from django.urls import path

from . import views

# LA URL EMPIEZA CON Noticias/ <este archivo>

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),

]