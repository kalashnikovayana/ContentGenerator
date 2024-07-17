# djangoProject/urls.py

from django.urls import path
from generator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('email_login/', views.email_login, name='email_login'),
    path('enter_otp/', views.enter_otp, name='enter_otp'),
    path('login/', views.custom_login, name='login'),
    path('enter_code/', views.enter_code, name='enter_code'),
]

