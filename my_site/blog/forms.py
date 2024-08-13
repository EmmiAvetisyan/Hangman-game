from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    labels = {
        "title":"Your street",
        "slug":"Your postal_code",
        "author":"Your city",
        "date":"your date",
        "rating":"your rating"
    }

    error_messages={
        "rating":{
            "required":"Your rating most not be empty!",
            "max_length":"Please enter a shorter rating!"
        }
    }