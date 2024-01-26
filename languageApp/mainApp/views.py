from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from .models import Content
from .models import Flashcard
# Create your views here.

def read_content(request):
    contents = Content.objects.all()
    return render(request, "mainApp/read_content.html", {'contents': contents})

def flashcards(request):
    flashcards = Flashcard.objects.all()
    return render(request, "mainApp/flashcards.html", {'flashcards': flashcards})

def translate(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')

        headers = {'Authorization': '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'}
        
        data = {
            "prompt": text + "\n\n###\n\nTranslate to Spanish:",
            "max_tokens": 60
        }

        response = requests.post('https://api.openai.com/v1/engines/davinci/completions', json=data, headers=headers)
        if response.status_code == 200:
                translated_text = response.json()['choices'][0]['text'].strip()
                return JsonResponse({'translated_text': translated_text})
        else:
            return JsonResponse({'error': 'Error from OpenAI API'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)