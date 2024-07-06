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
        "Navbar": Navbar.objects.all(),
        "Servicio": Servicio.objects.all()
    }
    return render(request, 'content/quienes-somos.html', context)

def vistaServicio(request):
    context = {
        "Navbar": Navbar.objects.all(),
        "Servicio": Servicio.objects.all()
    }
    return render(request, 'content/servicios.html', context)