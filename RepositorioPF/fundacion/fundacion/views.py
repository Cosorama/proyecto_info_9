from django.shortcuts import render
from apps.noticias.models import Noticia

def Home(request):
    ctx = {}
    ultimas_tres = Noticia.objects.filter().order_by('-id')[:3]
    ctx['notis'] = ultimas_tres
    return render(request, 'home.html', ctx)