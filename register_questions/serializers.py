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


class RegisterQuestionListSerializer(serializers.ModelSerializer):
    my_variant_questions = RegisterQuestionVariantSerializer(many=True)

    class Meta:
        model = RegisterQuestion
        fields = ["id", 'my_variant_questions']
