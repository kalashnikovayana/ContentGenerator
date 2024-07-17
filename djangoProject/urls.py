from django.urls import path
from generator.views import index, telegram_login

urlpatterns = [
    path('', index, name='index'),
    path('telegram_login/', telegram_login, name='telegram_login'),
]

