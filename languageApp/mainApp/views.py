from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from .models import Content
from .models import Flashcard
# Create your views here.

def view_content(request):
    contents = Content.objects.all()
    contentTitles = [content.title for content in contents]
    return render(request, "mainApp/view_content.html", {'titles': contentTitles})

def read_content(request):
    contents = Content.objects.all()
    context = {
        'title': 'Cha Cha Learning',
        'description': 'Welcome to Cha Cha Learning, your go-to platform for learning a new language. Whether you are a beginner or looking to enhance your language skills, we have resources and tools to make your language learning journey enjoyable and effective.',
        'cta': 'Get Started',
    }
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

def content(request):
    context = {
        'title': 'Cha Cha Learning',
        'description': 'Welcome to Cha Cha Learning, your go-to platform for learning a new language. Whether you are a beginner or looking to enhance your language skills, we have resources and tools to make your language learning journey enjoyable and effective.',
        'cta': 'Get Started',
    }
    return render(request, "mainApp/content.html")

def read_content(request):
    # Placeholder view for the 'Read' button
    return render(request, 'mainApp/read_content.html')

def flash_cards(request):
    # Placeholder view for the 'Flash Cards' button
    return render(request, 'mainApp/flash_cards.html')

def article1_display(request):
    return render(request, 'mainApp/article1_display.html')