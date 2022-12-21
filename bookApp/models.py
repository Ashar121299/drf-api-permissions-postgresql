from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    author=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Library(models.Model):
    
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)

    def __str__(self):
        return self.name