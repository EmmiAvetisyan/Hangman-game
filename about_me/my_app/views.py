from django.shortcuts import render
from django.http import HttpResponse
from .forms import Contactmessage
from .models import Contactmessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ProjectLinks



def home(request):
    return render (request, "my_app/index.html")

def about(request):
    return render (request, "my_app/index.html")

def contact(request):
    return render (request, "my_app/index.html")

def Pim(request):
    return render (request, "my_app/index.html")

def contactmessage(request):
    if request.method == 'POST':
        form = Contactmessage(request.POST)
        if form.is_valid():
            form.save() 
            return render(request, 'my_app/intex.html')
        else:
            return HttpResponse(request, "Fill out all the fields")
    else:
        form = Contactmessage()
    return render(request, 'my_app/intex.html', {'form': form})

def project_links(request):
    return render (request, "my_app/index.html", {
        "project_name" : ProjectLinks.project_name,
        "link" : ProjectLinks.link
    })