from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from .models import Noticia
# Create your views here.

def Listar(request):
    # Crear el diccionario para pasar datos al template
    ctx = {}
    # Buscar las noticias en la base de datos
    # Pasarlo al template

    todas = Noticia.objects.all()
    ctx['notis'] = todas
    
    return render(request, 'noticias/listar_noticias.html', ctx)
        

class Detalle_Noticia_Clase(LoginRequiredMixin, DetailView):
    model = Noticia
    template_name: 'noticias/noticia_detail.html'