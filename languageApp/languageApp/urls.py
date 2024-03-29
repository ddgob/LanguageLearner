"""
URL configuration for languageApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp.views import read_content
from mainApp.views import flashcards
from mainApp.views import translate
from mainApp.views import view_content, read_content, flashcards
from mainApp.views import content, read_content, flash_cards, article1_display

urlpatterns = [
    path('admin/', admin.site.urls),
    path('read_content', read_content),
    path('flash_cards', flashcards),
    path('translate/', translate, name='translate'),
    path('view_content', view_content),
    path('', content, name='content'),
    path('read/', read_content, name='read_content'),
    path('flash-cards/', flash_cards, name='flash_cards'),
    path('article1_display/', article1_display, name='article1_display'),
]