from django.db import models


# Create your models here.

class persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso = models.IntegerField()
    altura = models.IntegerField()
    email = models.CharField(max_length=100)