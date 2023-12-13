from django.contrib import admin
from .models import Question, QuestionVariant, QuestionSecondSide, QuestionPtichka, Question2variant, UserQuestions
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


@admin.register(UserQuestions)
class UserQuestionsAdmin(admin.ModelAdmin):
    pass


class Question2Admin(TranslationStackedInline):
    model = Question2variant
    extra = 2


class QuestionPtichkaAdmin(TranslationStackedInline):
    model = QuestionPtichka
    extra = 1

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class QuestionVariantAdmin(TranslationStackedInline):
    model = QuestionVariant
    extra = 1

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class QuestionSecondAdmin(TranslationStackedInline):
    model = QuestionSecondSide
    extra = 1

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    inlines = [QuestionVariantAdmin, QuestionSecondAdmin, QuestionPtichkaAdmin, Question2Admin]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
