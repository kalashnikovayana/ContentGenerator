from django.contrib import admin
from django.urls import path, include
from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('telegram_login/', views.telegram_login, name='telegram_login'),
    path('', include('generator.urls')),
]
