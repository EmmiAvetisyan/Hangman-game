from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.query import FlatValuesListIterable
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    text = models.CharField(max_length=1000)
    category = models.ManyToManyField(Category, blank=True, null=False)
    stock = models.IntegerField(
        validators=[MinValueValidator(-1000), MaxValueValidator(10000)])
    price = models.CharField(max_length=90000000)
    
    
    
    