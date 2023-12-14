from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator


class Country(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=123)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=123)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Invalid phone number')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=19, unique=True)
    name = models.CharField(max_length=350)
    last_name = models.CharField(max_length=132, null=True, blank=True)
    given_name = models.CharField(max_length=132, null=True, blank=True)
    date_birth = models.CharField(max_length=132, null=True, blank=True)
    passport_num = models.CharField(max_length=20, null=True, blank=True)
    passport_expire = models.CharField(max_length=20, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=223, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_completed_110 = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = ("Telefon raqamni tasdiqlash")
        verbose_name_plural = ("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name="Telefon raqam")
    code = models.CharField(max_length=10, verbose_name="Kod")

    def __str__(self):
        return self.phone


class PaymentAccounts(models.Model):
    amount = models.CharField(max_length=123)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Maxfiylik(models.Model):
    file = models.FileField(upload_to='files/')
