from django.urls import path
from .views import QuestionListAPIView, QuestionListAPIView2, CheckTestAPIView, UserQuestionsListAPIView

urlpatterns = [
    path('for-sidebar/', QuestionListAPIView.as_view()),
    path('by-id/<int:pk>/', QuestionListAPIView2.as_view()),
    path('check-test/', CheckTestAPIView.as_view()),
    path('result-test/', UserQuestionsListAPIView.as_view())
]
