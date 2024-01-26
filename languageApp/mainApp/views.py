from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def content(request):
    return render(request, "mainApp/content.html")