import imp
from django.contrib import admin
from .models import Evento, CategoriaEvento, CostoEvento, ModalidadEvento
# Register your models here.

admin.site.register(Evento)
admin.site.register(CategoriaEvento)
admin.site.register(CostoEvento)
admin.site.register(ModalidadEvento)