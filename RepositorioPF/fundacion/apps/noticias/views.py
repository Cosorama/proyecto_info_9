from django.shortcuts import render

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