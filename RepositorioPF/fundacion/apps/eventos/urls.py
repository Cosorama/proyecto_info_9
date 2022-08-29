from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('listar_eventos/', views.ListarEventos, name = 'listar_eventos'),
    path('detalle_evento/<int:pk>', views.Detalle_Evento_Clase.as_view(), name = 'evento_detail'),
]