from modeltranslation.translator import TranslationOptions, register
from .models import Question, QuestionVariant, QuestionPtichka, QuestionSecondSide, Question2variant


@register(Question2variant)
class Question3(TranslationOptions):
    fields = ('name',)


@register(Question)
class Question(TranslationOptions):
    fields = ('name', 'second_name')


@register(QuestionVariant)
class QuestionVariant(TranslationOptions):
    fields = ('name',)


@register(QuestionPtichka)
class QuestionPtichka(TranslationOptions):
    fields = ('name',)


@register(QuestionSecondSide)
class QuestionSecondSide(TranslationOptions):
    fields = ('second_side_1', 'second_side_2', 'second_side_3', 'variant_1', 'variant_2')
