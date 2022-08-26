from pathlib import Path
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('listar/', views.Listar, name = 'listar_noticias'),
    path('detalle/<int:pk>', views.Detalle_Noticia_Clase.as_view(), name = 'noticia_detail'),
    path('add_comentario/<int:pk>', views.Agregar_Comentario, name="agregar_comentario"),
]