from django.shortcuts import render
from .models import *

# Create your views here.

def vistaInicio(request):
    context = {
        "Navbar": Navbar.objects.all()
    }
    return render(request, 'content/inicio.html', context)

def vistaAbout(request):
    context = {
        "Navbar": Navbar.objects.all()
    }
    return render(request, 'content/quienes-somos.html', context)

def vistaContacto(request):
    context = {
        "Navbar": Navbar.objects.all()
    }
    return render(request, 'content/servicios.html', context)