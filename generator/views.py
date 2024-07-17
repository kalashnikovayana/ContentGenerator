from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.conf import settings
import telegram
import requests
import random
import string

def generate_password(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def telegram_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        chat_id = request.POST.get('chat_id')
        user = User.objects.filter(username=username).first()
        if user:
            login(request, user)
            return redirect('index')
        else:
            password = generate_password()
            user = User.objects.create_user(username=username, password=password)
            bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
            bot.send_message(chat_id=chat_id, text=f'Ваш логін: {username}\nВаш пароль: {password}')
            login(request, user)
            return redirect('index')
    return render(request, 'telegram_login.html')

def generate_content(prompt):
    api_key = settings.OPENAI_API_KEY
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': prompt,
        'max_tokens': 150,
    }
    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)
    return response.json().get('choices')[0].get('text')

def index(request):
    content = None
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        content = generate_content(prompt)
    return render(request, 'index.html', {'content': content})
