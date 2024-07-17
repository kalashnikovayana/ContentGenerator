# djangoProject/urls.py

from django.urls import path
from generator.views import index, telegram_login, custom_login, enter_code

urlpatterns = [
    path('', index, name='index'),
    path('telegram_login/', telegram_login, name='telegram_login'),
    path('login/', custom_login, name='login'),
    path('enter_code/', enter_code, name='enter_code'),
]

