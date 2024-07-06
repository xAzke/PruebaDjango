from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vistaInicio, name="index"),
    path('quienes-somos', views.vistaAbout, name="quienes-somos"),
    path('servicios', views.vistaServicio, name="servicios"),
]
