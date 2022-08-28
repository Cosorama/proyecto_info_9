from os import truncate
from pickle import TRUE
from queue import Empty
from django import forms
from .models import Categoria

class FiltroCategoriaNoticia(forms.Form):
    categoria = forms.ModelChoiceField(queryset = Categoria.objects.all())