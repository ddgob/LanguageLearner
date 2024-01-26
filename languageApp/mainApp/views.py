from django.shortcuts import render
from django.http import HttpResponse
from .models import Content
from .models import Flashcards
# Create your views here.

def read_content(request):
    contents = Content.objects.all()
    return render(request, "mainApp/read_content.html", {'contents': contents})

def flashcards(request):
    flashcards = Flashcards.objects.all()
    return render(request, "mainApp/flashcards.html", {'flashcards': flashcards})