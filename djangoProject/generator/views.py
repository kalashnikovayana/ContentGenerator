import requests
from django.shortcuts import render

def generate_content(prompt):
    api_key = 'YOUR_OPENAI_API_KEY'  # замініть 'YOUR_OPENAI_API_KEY' на ваш API ключ
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
    return render(request, 'generator/index.html', {'content': content})
