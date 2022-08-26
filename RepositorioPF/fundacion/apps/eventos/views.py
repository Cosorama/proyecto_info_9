from django.shortcuts import render

from .models import Evento
# Create your views here.

def ListarEventos(request):
    
    ctx = {}
    todas = Evento.objects.all()
    ctx['eventos'] = todas
    
    return render(request, 'eventos/listar_eventos.html', ctx)