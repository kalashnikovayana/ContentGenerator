from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PhoneNumberForm
from .models import UserProfile
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
        niche = request.POST.get('niche')
        audience = request.POST.get('audience')
        content_type = request.POST.get('content_type')

        if content_type == 'content_plan':
            prompt = (
                f"Аналізуй нішу {niche} та цільову аудиторію {audience}. "
                f"Визнач сегменти ринку, характеристики цільової аудиторії, їх болі та вигоди. "
                f"На основі цього аналізу сформуй контент-план на 7 днів, "
                f"включаючи дату, тему посту, рекламне повідомлення, опис контенту та пропозиції графічного зображення."
            )
            max_tokens = 300
        elif content_type == 'post':
            prompt = (
                f"Створи пост для ніші {niche} та цільової аудиторії {audience}. "
                f"Включи аналіз цільової аудиторії, визнач сегменти, характеристики, болі та вигоди. "
                f"На основі цього сформуй зміст посту."
            )
            max_tokens = 50

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.5,
            n=1
        )
        generated_text = response.choices[0].text.strip()
        return render(request, 'generator/index.html', {'generated_text': generated_text})
    return render(request, 'generator/index.html')

@csrf_exempt
def telegram_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        code = ''.join(random.choices(string.digits, k=6))
        request.session['verification_code'] = code
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.phone_number = phone_number
        user_profile.is_paid = True
        user_profile.save()
        # Логіка для відправки коду через Telegram
        return redirect('enter_code')
    return render(request, 'generator/telegram_login.html')

@csrf_exempt
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'generator/login.html', {'error': 'Invalid credentials'})
    return render(request, 'generator/login.html')

@csrf_exempt
def enter_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == request.session.get('verification_code'):
            return redirect('index')
        else:
            return render(request, 'generator/enter_code.html', {'error': 'Invalid code'})
    return render(request, 'generator/enter_code.html')
