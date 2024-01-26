from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Flashcard(models.Model):
    originalText = models.CharField(max_length=250)
    translatedText = models.CharField(max_length=250)

    def __str__(self):
        return self.originalText