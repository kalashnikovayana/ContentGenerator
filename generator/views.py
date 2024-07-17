from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import random
import string

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
            engine="davinci-codex",
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
        # Send username and password to the user via Telegram bot (not implemented here)
        return HttpResponse(f'Login: {username}, Password: {password}')
    return render(request, 'generator/telegram_login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate user (logic not implemented here)
        # Redirect to the main page after successful login
        return redirect('index')
    return render(request, 'generator/login.html')
