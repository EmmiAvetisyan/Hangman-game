from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<str:m>", views.e, name="about-me")
]
