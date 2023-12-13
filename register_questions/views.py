from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RegisterQuestion, RegisterQuestionVariant
from .serializers import RegisterQuestionSerializer, RegisterQuestionVariantSerializer
from rest_framework import authentication, permissions

QUESTION_INDEX = [
    '10.1.0', '10.1.1', '10.1.2'
]


class RegisterQuestionCreateAPIView(generics.CreateAPIView):
    queryset = RegisterQuestion.objects.all()
    serializer_class = RegisterQuestionSerializer


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
