from .models import Question, Question2variant, QuestionPtichka, QuestionVariant, QuestionSecondSide, UserQuestions
from rest_framework import serializers


class Question2variantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question2variant
        fields = ['name']


class QuestionPtichkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPtichka
        fields = ['name']


class QuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVariant
        fields = ['name']


class QuestionSecondSideSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSecondSide
        fields = ['second_side_1', 'second_side_2', 'second_side_3', 'variant_1', 'variant_2']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'name']


class QuestionSerializer2(serializers.ModelSerializer):
    for_question_2 = Question2variantSerializer(many=True)
    for_done_front = QuestionPtichkaSerializer(many=True)
    answer_variants = QuestionVariantSerializer(many=True)
    second_side_question = QuestionSecondSideSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'name', 'second_name', 'for_done_front', 'answer_variants', 'second_side_question',
                  'for_question_2']


class UserQuestionsSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False)

    class Meta:
        model = UserQuestions
        fields = ['id', 'question', 'answer']
