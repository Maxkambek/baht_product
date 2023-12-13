from django.urls import path
from .views import LoginAPI, RegisterAPI, RegisterConfirmAPI, RegionListAPIView, DistrictListAPIView, \
    CountryListAPIView, CreateUserAPIView, AccountRUDAPIView

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('register-confirm/', RegisterConfirmAPI.as_view()),
    path('regions/', RegionListAPIView.as_view()),
    path('districs/', DistrictListAPIView.as_view()),
    path('country/', CountryListAPIView.as_view()),
    path('create-user/', CreateUserAPIView.as_view()),
    path('user-rud/', AccountRUDAPIView.as_view())
]
