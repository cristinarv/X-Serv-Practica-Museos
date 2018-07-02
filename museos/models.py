from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Museo(models.Model):
	# Descripción de los datos de la organización(museo):
    nombre = models.CharField(max_length=100)
    id_entidad = models.IntegerField(null=True)
    descripcion = models.TextField(null=True)
    horario = models.TextField(null=True)
    transporte = models.TextField(null=True)
    accesibilidad = models.IntegerField(null=True)    
    url = models.URLField(null=True)
    # Descripción de la dirección
    direccion = models.CharField(max_length=64, null=True)
    barrio = models.CharField(max_length=64, null=True)
    distrito = models.CharField(max_length=64, null=True)
    # Descripción del contacto
    telefono = models.CharField(max_length=64, null=True)
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    museo = models.ForeignKey(Museo)
    comentario = models.TextField()
    publicacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return str(self.publicacion)

class Content_User(models.Model):
    usuario = models.ForeignKey(User)
    museo = models.ForeignKey(Museo)
    fecha = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.usuario.username

class Configuracion(models.Model):
    color = models.CharField(max_length=64)
    titulo = models.CharField(max_length=100)
    usuario = models.ForeignKey(User)
    tamano = models.CharField(max_length=64)
    def __str__(self):
        return self.usuario.username
