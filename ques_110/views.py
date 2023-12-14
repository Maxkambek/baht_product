from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Account
from .models import Question, UserQuestions
from .serializer import QuestionSerializer, QuestionSerializer2, UserQuestionsSerializer
from rest_framework import generics, permissions, authentication


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListAPIView2(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer2


class CheckTestAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user.id
        print(user)
        data = self.request.data['question_id']
        data1 = self.request.data['yes_or_no']
        qs = UserQuestions.objects.filter(user_id=user, question_id=data).first()
        if not qs:
            new = UserQuestions.objects.create(
                question_id=data,
                user_id=user,
                answer=data1
            )
            new.save()
        if data == 109:
            acc = Account.objects.filter(id=user).first()
            acc.is_completed_110 = True
            acc.save()
        return Response('success', status=200)


class UserQuestionsListAPIView(generics.ListAPIView):
    serializer_class = UserQuestionsSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = UserQuestions.objects.filter(user=self.request.user)
        return queryset
