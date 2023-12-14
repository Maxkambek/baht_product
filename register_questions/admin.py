from django.contrib import admin
from .models import RegisterQuestion, RegisterQuestionVariant


class RegisterQuestionVariantInline(admin.StackedInline):
    model = RegisterQuestionVariant


@admin.register(RegisterQuestion)
class RegisterQuestionAdmin(admin.ModelAdmin):
    inlines = [RegisterQuestionVariantInline]
