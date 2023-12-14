from rest_framework import serializers
from .models import Account, VerifyPhone, Country, Region, District, Maxfiylik


class MaxfiylikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maxfiylik
        fields = ['id', 'file']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'country']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'region']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone']


class VerifyPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyPhone
        fields = ['phone', 'code']


class VerifyPhoneSerializer2(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=8)

    class Meta:
        model = VerifyPhone
        fields = ['phone', 'code', 'password']


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=8)

    class Meta:
        model = Account
        fields = ['phone', 'password']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone', 'name', 'is_paid']
