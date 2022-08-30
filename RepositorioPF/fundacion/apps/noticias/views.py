from cmath import log
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import FiltroCategoriaNoticia, FiltroFechaNoticia
from django.db.models import Q
from .models import Noticia, Comentario
# Create your views here.

def Listar(request):
    # Crear el diccionario para pasar datos al template
    ctx = {}
    # Buscar las noticias en la base de datos
    # Pasarlo al template
    filtro = FiltroCategoriaNoticia()
    ctx['formulario_filtro'] = filtro

    filtro_fecha = FiltroFechaNoticia()
    ctx['formulario_fecha'] = filtro_fecha
    
    todas = Noticia.objects.all() # si quiero que me traiga menos noticias --> [:3] 
    
    filter_date = request.GET.get("fecha")
    filtro_categoria = request.GET.get("categoria")
    
    
    if filtro_categoria:
        todas = Noticia.objects.filter(categoria = filtro_categoria)
    elif filter_date:
        todas = Noticia.objects.filter(creado = filter_date)
    else:
        todas = Noticia.objects.filter().order_by('-id')
    ctx['notis'] = todas
    
    
    return render(request, 'noticias/listar_noticias.html', ctx)
        

class Detalle_Noticia_Clase(DetailView):
    model = Noticia
    template_name: 'noticias/noticia_detail.html'


@login_required
def Agregar_Comentario(request,pk):
	texto_comentario = request.POST.get('coment')
	
	#Forma 1 (es la mejor para este caso)
	noti = Noticia.objects.get(pk = pk)

	Comentario.objects.create(noticia = noti, texto = texto_comentario, usuario = request.user)

	return HttpResponseRedirect(reverse_lazy('noticias:noticia_detail' , kwargs={'pk':pk}))
