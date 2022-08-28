from ast import Mod
from statistics import mode
from django.db import models

# Create your models here.

class CategoriaEvento(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nombre

class ModalidadEvento(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class CostoEvento(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    titulo = models.CharField(max_length=120)
    detalle = models.TextField()
    imagen = models.ImageField(upload_to='eventos', null=True, blank=True)
    categoria = models.ForeignKey(CategoriaEvento, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    modalidad = models.ForeignKey(ModalidadEvento, on_delete=models.CASCADE, null=True)
    lugar = models.CharField(max_length=120, null=True, blank=True)
    costo = models.ForeignKey(CostoEvento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo