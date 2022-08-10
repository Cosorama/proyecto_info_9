from django.contrib import admin
from .models import Categoria, Noticia

# Register your models here.

admin.site.register(Noticia)
admin.site.register(Categoria)