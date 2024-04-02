from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    auteur = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now())

