from distutils.command.upload import upload
from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=120)
    creado = models.DateField(auto_now_add=True)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to='noticias', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

    def obtener_mis_comentarios(self):
        return self.mis_comentarios.all()


class Comentario(models.Model):
	noticia = models.ForeignKey(Noticia, related_name = 'mis_comentarios', on_delete = models.CASCADE)
	texto = models.TextField()
	creado = models.DateTimeField(auto_now_add = True)
	usuario = models.ForeignKey(Usuario, related_name = 'usuario_comentario' , on_delete = models.CASCADE)

	def __str__(self):
		return self.texto