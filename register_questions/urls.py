from django.urls import path
from .views import RegisterQuestionVariantCreateAPIView, RegisterQuestionCreateAPIView, RegisterQuestionStatistics

urlpatterns = [
    path('question/', RegisterQuestionCreateAPIView.as_view()),
    path('question-variant/', RegisterQuestionVariantCreateAPIView.as_view()),
    path('for-chart/', RegisterQuestionStatistics.as_view())
]
