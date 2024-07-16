from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
import telegram
import random
import string

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def telegram_login(request):
    if request.method == 'POST':
        token = settings.TELEGRAM_TOKEN
        bot = telegram.Bot(token=token)
        username = request.POST.get('username')
        chat_id = request.POST.get('chat_id')

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
        else:
            password = generate_random_password()
            user = User.objects.create_user(username=username, password=password)
            user.save()
            bot.send_message(chat_id=chat_id, text=f'Your login details:\nUsername: {username}\nPassword: {password}')

        return redirect('index')
    return render(request, 'telegram_login.html')
