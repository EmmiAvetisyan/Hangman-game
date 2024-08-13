from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


about_me = {
    "home": "",
    "about" : "👋 Hi, I'm Emmi",
    "contact": " 📱 My phone number: 093101785"
}

def index(request):
    i = list(about_me.keys())
    
    return render(request, "challenges/index.html", {
        "i" : i
    })
    
def e(request, m):
    try:
        about_text = about_me[m]
        return render(request, "challenges/challenge.html", {
            "text" : about_text,
            "me_name" : m
        })
    except:
        return HttpResponseNotFound("<h1> This week is not supported!</h1>")

