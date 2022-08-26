from cmath import log
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


from .models import Noticia, Comentario
# Create your views here.

def Listar(request):
    # Crear el diccionario para pasar datos al template
    ctx = {}
    # Buscar las noticias en la base de datos
    # Pasarlo al template

    todas = Noticia.objects.all()
    ctx['notis'] = todas
    
    return render(request, 'noticias/listar_noticias.html', ctx)
        

class Detalle_Noticia_Clase (DetailView):
    model = Noticia
    template_name: 'noticias/noticia_detail.html'


@login_required
def Agregar_Comentario(request,pk):
	texto_comentario = request.POST.get('coment')
	
	#Forma 1 (es la mejor para este caso)
	noti = Noticia.objects.get(pk = pk)

	c = Comentario.objects.create(noticia = noti, texto = texto_comentario, usuario = request.user)

	return HttpResponseRedirect(reverse_lazy('noticias:noticia_detail' , kwargs={'pk':pk}))