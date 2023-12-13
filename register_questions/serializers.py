from .models import RegisterQuestion, RegisterQuestionVariant
from rest_framework import serializers


class RegisterQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterQuestion
        fields = '__all__'


class RegisterQuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterQuestionVariant
        fields = '__all__'
