from django import forms
from .models import CategoriaEvento

class FiltroCategoria(forms.Form):
    categoria = forms.ModelChoiceField(queryset = CategoriaEvento.objects.all())