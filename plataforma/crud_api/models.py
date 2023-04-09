from django.db import models
import datetime

# modelo Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    profesor = models.CharField(max_length=255)
    fecha = models.DateField()
    
# modelo Curso
class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    telefono = models.IntegerField()
    pais = models.CharField(max_length=30)
    datetime.datetime.now()
    
    