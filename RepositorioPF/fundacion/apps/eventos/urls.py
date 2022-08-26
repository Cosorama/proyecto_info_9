from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('listar_eventos/', views.ListarEventos, name = 'listar_eventos'),
]