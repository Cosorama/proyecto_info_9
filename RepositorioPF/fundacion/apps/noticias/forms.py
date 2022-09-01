from os import truncate
from pickle import TRUE
from queue import Empty
from django import forms
from .models import Categoria
from django.contrib.admin.widgets import AdminDateWidget


class FiltroCategoriaNoticia(forms.Form):
    categoria = forms.ModelChoiceField(queryset = Categoria.objects.all())

class FiltroFechaNoticia(forms.Form):
    fecha = forms.DateField(widget=AdminDateWidget)