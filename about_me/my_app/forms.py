from django import forms

from .models import Contactmessage


class Contactmessage(forms.ModelForm):
    class Meta:
        model = Contactmessage
        fields = "__all__"
        labels = {
            "name": "Your name",
            "email": "Your email",
            "message": " Message",
            "number" : "Phone number"
        }
