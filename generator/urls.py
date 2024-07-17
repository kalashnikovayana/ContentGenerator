from django.urls import path
from generator.views import index, telegram_login, login_view

urlpatterns = [
    path('', login_view, name='login'),
    path('index/', index, name='index'),
    path('telegram_login/', telegram_login, name='telegram_login'),
]

