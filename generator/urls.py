from django.urls import path
from .views import index, telegram_login, custom_login, enter_code, save_phone_number

urlpatterns = [
    path('', index, name='index'),
    path('telegram_login/', telegram_login, name='telegram_login'),
    path('login/', custom_login, name='login'),
    path('enter_code/', enter_code, name='enter_code'),
    path('save_phone_number/', save_phone_number, name='save_phone_number'),
]

