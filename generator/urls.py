from django.urls import path
from .views import telegram_login, index

urlpatterns = [
    path('login/', telegram_login, name='telegram_login'),
    path('', index, name='index'),
]

