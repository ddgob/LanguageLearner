from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def content(request):
    context = {
        'title': 'Cha Cha Learning',
        'description': 'Welcome to Cha Cha Learning, your go-to platform for learning a new language. Whether you are a beginner or looking to enhance your language skills, we have resources and tools to make your language learning journey enjoyable and effective.',
        'cta': 'Get Started',
    }
    return render(request, "mainApp/content.html")

