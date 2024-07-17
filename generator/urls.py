from django.urls import path
from .views import index, email_login, enter_otp

urlpatterns = [
    path('', index, name='index'),
    path('email_login/', email_login, name='email_login'),
    path('enter_otp/', enter_otp, name='enter_otp'),
]


