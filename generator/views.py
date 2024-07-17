from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import openai
import random
import string
from .forms import EmailLoginForm, OTPForm
from django.core.mail import send_mail
from django_otp.plugins.otp_email.models import EmailDevice

openai.api_key = 'your-openai-api-key'

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
def email_login(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            device, created = EmailDevice.objects.get_or_create(user=request.user, email=email)
            otp = ''.join(random.choices(string.digits, k=6))
            device.token = otp
            device.save()
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            request.session['email'] = email
            return redirect('enter_otp')
    else:
        form = EmailLoginForm()
    return render(request, 'generator/email_login.html', {'form': form})

@csrf_exempt
def enter_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            email = request.session.get('email')
            device = EmailDevice.objects.get(email=email)
            if device.verify_token(otp):
                login(request, device.user)
                return redirect('index')
            else:
                return render(request, 'generator/enter_otp.html', {'form': form, 'error': 'Invalid OTP'})
    else:
        form = OTPForm()
    return render(request, 'generator/enter_otp.html', {'form': form})

