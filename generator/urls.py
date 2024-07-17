from django.urls import path
from .views import index, telegram_login, user_login

urlpatterns = [
    path('', index, name='index'),
    path('telegram_login/', telegram_login, name='telegram_login'),
    path('login/', user_login, name='login'),
]
