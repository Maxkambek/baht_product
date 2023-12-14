from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from accounts.models import Account
from .models import RegisterQuestion, RegisterQuestionVariant
from .serializers import RegisterQuestionSerializer, RegisterQuestionVariantSerializer, RegisterQuestionListSerializer
from rest_framework import authentication, permissions

QUESTION_INDEX = [
    '10.1.0', '10.1.1', '10.1.2'
]


class RegisterQuestionListAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        queryset = RegisterQuestion.objects.filter(account=self.request.user).first()
        data = RegisterQuestionVariant.objects.filter(question=queryset)
        serializer = RegisterQuestionVariantSerializer(data, many=True)
        return Response(serializer.data)


class RegisterQuestionCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        data = request.data
        ques = RegisterQuestion.objects.filter(account_id=self.request.user.id).first()
        if not ques:
            ques = RegisterQuestion.objects.create(
                account_id=self.request.user.id,
                last_name=data['last_name'],
                first_name=data['first_name'],
                given_name=data['given_name'],
                age=data['age'],
                address=data['address'],
                phone=data['phone'],
                eduction=data['eduction'],
                family_status=data['family_status'],
                children=data['children'],
                social_status=data['social_status']
            )
            ques.save()
        variants = self.request.data['variant_data']
        for i in list(variants):
            if not RegisterQuestionVariant.objects.filter(question_id=ques.id, index_question=i['key']):
                variant = RegisterQuestionVariant.objects.create(
                    question_id=ques.id,
                    variant_name=i['value'],
                    index_question=i['key']
                )
                variant.save()
        user = Account.objects.filter(id=self.request.user.id).first()
        user.is_completed = True
        user.save()
        return Response("Success", status=status.HTTP_201_CREATED)


# class RegisterQuestionCreateAPIView(generics.CreateAPIView):
#     queryset = RegisterQuestion.objects.all()
#     serializer_class = RegisterQuestionSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]
#
#     def create(self, request, *args, **kwargs):
#         data = request.data
#         data['account'] = request.user.id
#         exist = RegisterQuestion.objects.filter(account_id=request.user.id).first()
#         if exist:
#             return Response({"error": "error"})
#         user = Account.objects.filter(id=self.request.user.id).first()
#         user.is_completed = True
#         user.save()
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#     def get_success_headers(self, data):
#         try:
#             return {'Location': str(data[api_settings.URL_FIELD_NAME])}
#         except (TypeError, KeyError):
#             return {}


class RegisterQuestionVariantCreateAPIView(generics.CreateAPIView):
    queryset = RegisterQuestionVariant.objects.all()
    serializer_class = RegisterQuestionVariantSerializer


class RegisterQuestionStatistics(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Response({'message': 'You are not us'}, status=403)
        data = {}
        for i in QUESTION_INDEX:
            count = RegisterQuestionVariant.objects.filter(index_question=i).count()
            name = RegisterQuestionVariant.objects.filter(index_question=i).first()
            try:
                data[name.variant_name] = {
                    'index': i,
                    'count': count
                }
            except:
                pass
        return Response(data, status=200)
