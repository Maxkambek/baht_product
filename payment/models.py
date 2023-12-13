import uuid
from django.db import models
from accounts.models import Account


class Order(models.Model):
    TYPE_ORDER = (
        ('full', 'full'),
        ('month', 'month'),
        ('week', 'week')
    )
    client = models.ForeignKey(Account, on_delete=models.CASCADE)
    type_order = models.CharField(choices=TYPE_ORDER, max_length=123)
    order_time = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'
