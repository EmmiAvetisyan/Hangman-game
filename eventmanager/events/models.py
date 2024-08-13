from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    owner = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title 

