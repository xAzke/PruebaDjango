from django.db import models

# Create your models here.

class Navbar(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=100)