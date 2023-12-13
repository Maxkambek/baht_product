from django.db import models
from ckeditor.fields import RichTextField

from accounts.models import Account


class Question(models.Model):
    name = RichTextField()
    second_name = models.CharField(max_length=333, null=True, blank=True)

    def __str__(self):
        return f'{self.id}'


class Question2variant(models.Model):
    name = RichTextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='for_question_2')

    def __str__(self):
        return self.name


class QuestionPtichka(models.Model):
    name = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='for_done_front')


class QuestionVariant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_variants')
    name = models.TextField()


class QuestionSecondSide(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='second_side_question')
    second_side_1 = models.TextField()
    second_side_2 = models.TextField()
    second_side_3 = models.TextField()
    variant_1 = models.TextField()
    variant_2 = models.TextField()


class UserQuestions(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'
