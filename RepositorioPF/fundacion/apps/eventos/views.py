from django.shortcuts import render
from django.db.models import QuerySet
from .forms import FiltroCategoriaEvento
from .models import Evento
from django.views.generic.detail import DetailView
# Create your views here.

def ListarEventos(request):

    formulario = FiltroCategoriaEvento()
    
    ctx = {}
    
    ctx['form'] = formulario

    categoria = request.GET.get("categoria")
    
    if categoria:
        todas = Evento.objects.filter(categoria = categoria)
    else:
        todas = Evento.objects.filter().order_by('-id')
    ctx['eventos'] = todas

    return render(request, 'eventos/listar_eventos.html', ctx)

class Detalle_Evento_Clase(DetailView):
    model = Evento
    template_name: 'eventos/evento_detail.html'