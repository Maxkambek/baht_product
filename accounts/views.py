from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Country, Region, District, Account, VerifyPhone, Maxfiylik
from .serializer import CountrySerializer, RegionSerializer, DistrictSerializer, RegisterSerializer, LoginSerializer, \
    VerifyPhoneSerializer, AccountSerializer, VerifyPhoneSerializer2, MaxfiylikSerializer
from rest_framework import generics, status, permissions
from rest_framework.views import Response
from random import randint
from .utils import verify


class MaxfiylikListAPIView(generics.ListAPIView):
    queryset = Maxfiylik.objects.all()
    serializer_class = MaxfiylikSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        true_phone = '+'
        for i in str(phone):
            if i.isalnum():
                true_phone = true_phone + i
        if not phone:
            return Response({'Telefon raqam kemadi tupoymisz?'}, status=404)
        if Account.objects.filter(phone=true_phone, is_active=True).first():
            return Response({'message': "This number already exist"}, status=status.HTTP_302_FOUND)
        ver = VerifyPhone.objects.filter(phone=phone).first()
        if ver:
            ver.delete()
        else:
            code = str(randint(1000, 10000))
            verify(true_phone, code)
            VerifyPhone.objects.create(phone=true_phone, code=code)
        return Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                        status=status.HTTP_200_OK)


class RegisterConfirmAPI(generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = VerifyPhoneSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        code = self.request.data['code']
        true_phone = '+'
        for i in str(phone):
            if i.isalnum():
                true_phone = true_phone + i
        v = VerifyPhone.objects.filter(phone=true_phone, code=code).first()
        if not v:
            return Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': "Confirmation code correct!"}, status=status.HTTP_200_OK)


class CreateUserAPIView(generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = VerifyPhoneSerializer2

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        true_phone = '+'
        for i in str(phone):
            if i.isalnum():
                true_phone = true_phone + i
        code = self.request.data['code']
        password = self.request.data['password']
        v = VerifyPhone.objects.filter(phone=true_phone, code=code).first()
        if v:
            v.delete()
        else:
            return Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        user = Account.objects.create(
            phone=true_phone,
            password=password
        )
        user.is_active = True
        user.save()
        token = Token.objects.create(user=user)
        data = {
            'message': 'User verified',
            'token': str(token.key),
            'is_paid': user.is_paid
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    def get_queryset(self):
        return Account.objects.all()

    def get_serializer_class(self):
        return LoginSerializer

    def post(self, request, *args, **kwargs):
        phone = request.data['phone']
        pas = request.data['password']
        true_phone = '+'
        for i in str(phone):
            if i.isalnum():
                true_phone = true_phone + i
        user = Account.objects.filter(phone=true_phone, password=pas).first()
        if not user:
            return Response({'message': 'Login yoki parol xatoro sal'}, status=status.HTTP_404_NOT_FOUND)
        token = Token.objects.get(user=user)
        data = dict()
        data['token'] = token.key
        data['success'] = True
        data['is_paid'] = user.is_paid
        data['is_completed'] = user.is_completed
        data['is_completed_110'] = user.is_completed_110
        return Response(data, status=status.HTTP_200_OK)


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionListAPIView(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get_queryset(self):
        queryset = Region.objects.all()
        country_id = self.request.GET.get('country_id')
        if country_id:
            queryset = queryset.filter(country_id=country_id)
        return queryset


class DistrictListAPIView(generics.ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        country_id = self.request.GET.get('district_id')
        if country_id:
            queryset = queryset.filter(region_id=country_id)
        return queryset


class AccountRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.request.user, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.request.user
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
