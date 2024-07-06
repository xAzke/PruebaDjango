from django.db import models

# Create your models here.

class Navbar(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

class Servicio(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    contenido_lista = models.JSONField()
    url_img = models.TextField()

class About(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()