from django.contrib import admin
from .models import Account, Country, Region, District, VerifyPhone, PaymentAccounts


@admin.register(PaymentAccounts)
class PaymentAccountsAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(VerifyPhone)
class VerifyPhoneAdmin(admin.ModelAdmin):
    pass
