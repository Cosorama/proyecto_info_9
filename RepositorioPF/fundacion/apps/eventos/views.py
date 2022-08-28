from django.shortcuts import render
from django.db.models import QuerySet
from .forms import FiltroCategoriaEvento
from .models import Evento
# Create your views here.

def ListarEventos(request):

    formulario = FiltroCategoriaEvento()
    
    ctx = {}
    
    ctx['form'] = formulario

    categoria = request.GET.get("categoria")
    
    if categoria:
        todas = Evento.objects.filter(categoria = categoria)
    else:
        todas = Evento.objects.all()
    ctx['eventos'] = todas

    return render(request, 'eventos/listar_eventos.html', ctx)