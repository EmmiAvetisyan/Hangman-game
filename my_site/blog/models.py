from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    author = models.CharField(max_length=100)
    text = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])


    def __str__(self):
        return f"{self.title} by {self.author}"
