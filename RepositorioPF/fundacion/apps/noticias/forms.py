from os import truncate
from pickle import TRUE
from queue import Empty
from django import forms

from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget

from .models import Categoria, Noticia


class FiltroCategoriaNoticia(forms.Form):
    categoria = forms.ModelChoiceField(queryset = Categoria.objects.all())

class FiltroFechaNoticia(forms.Form):
    fecha = forms.DateField()