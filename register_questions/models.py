from django.db import models
from accounts.models import Account


class RegisterQuestion(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    last_name = models.CharField(max_length=123, null=True)
    first_name = models.CharField(max_length=123, null=True)
    given_name = models.CharField(max_length=123, null=True)
    age = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=233, null=True)
    phone = models.CharField(max_length=22, null=True)
    eduction = models.CharField(max_length=123, null=True)
    family_status = models.CharField(max_length=223, null=True)
    children = models.CharField(max_length=123, null=True)
    social_status = models.CharField(max_length=123, null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.given_name}'


class RegisterQuestionVariant(models.Model):
    question = models.ForeignKey(RegisterQuestion, on_delete=models.CASCADE, related_name='my_variant_questions')
    index_question = models.CharField(max_length=123, null=True)
    variant_name = models.CharField(max_length=333, null=True)

    def __str__(self):
        return self.index_question
