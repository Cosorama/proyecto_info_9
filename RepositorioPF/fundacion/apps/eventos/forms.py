from django import forms
from .models import CategoriaEvento

class FiltroCategoriaEvento(forms.Form):
    categoria = forms.ModelChoiceField(queryset = CategoriaEvento.objects.all())