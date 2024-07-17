from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import random
import string
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

openai.api_key = 'your-openai-api-key'

def generate_random_credentials():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    return username, password

@csrf_exempt
def index(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        content = response.choices[0].text.strip()
        return render(request, 'generator/index.html', {'content': content})
    return render(request, 'generator/index.html')

@csrf_exempt
def telegram_login(request):
    if request.method == 'POST':
        # Simulate user authentication after payment
        username, password = generate_random_credentials()
        # Save user to the database
        user = User.objects.create_user(username=username, password=password)
        # Send username and password to the user via Telegram bot (not implemented here)
        return HttpResponse(f'Login: {username}, Password: {password}')
    return render(request, 'generator/telegram_login.html')

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'generator/login.html')
