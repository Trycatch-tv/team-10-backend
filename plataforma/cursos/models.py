from django.db import models
from django.core.exceptions import ValidationError


# Create your models here
class Categoria(models.Model):
    nombre=models.CharField(max_length=50, unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    # Verificar si ya existe una categoria con el mismo nombre
    def clean(self):
        categoria_con_mismo_nombre = Categoria.objects.filter(nombre=self.nombre)
        if self.id:
            categoria_con_mismo_nombre = categoria_con_mismo_nombre.exclude(id=self.id)
        if categoria_con_mismo_nombre.exists():
            raise ValidationError('Ya existe una categoria con este nombre.')

    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre


    
    

class Estudiante(models.Model):
    nombre=models.CharField(max_length=200, unique=True)
    email=models.EmailField(max_length=100, unique=True)
    created_at=models.TimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    # Verificar si ya existe un estudiante con el mismo nombre
    def clean(self):
        estudiante_con_mismo_nombre = Estudiante.objects.filter(nombre=self.nombre)
        if self.id:
            estudiante_con_mismo_nombre = estudiante_con_mismo_nombre.exclude(id=self.id)
        if estudiante_con_mismo_nombre.exists():
            raise ValidationError('Ya existe un estudiante con este nombre.')
    
    
    
    @property
    def cursos_details(self):
        return self.curso.all() 
    
    class Meta:
        verbose_name='estudiante'
        verbose_name_plural='estudiantes'
        
    def __str__(self):
        return self.nombre    
    
class Curso(models.Model):
    title=models.CharField(max_length=200, unique=True)
    description=models.TextField(max_length=500)
    tutor=models.CharField(max_length=200)
    categoria=models.ManyToManyField(Categoria)
    fechaInicio=models.DateField(auto_created=False)
    fechaFinalizacion=models.DateField(auto_created=False)
    created_at=models.TimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    #imagen=models.ImageField(upload_to='Curso', null=True, blank=True)

    # Verificar si ya existe un curso con el mismo nombre
    def clean(self):
        curso_con_mismo_nombre = Estudiante.objects.filter(nombre=self.nombre)
        if self.id:
            curso_con_mismo_nombre  = curso_con_mismo_nombre .exclude(id=self.id)
        if curso_con_mismo_nombre .exists():
            raise ValidationError('Ya existe un curso con este nombre.')
    
    
    class Meta:
        verbose_name='curso'
        verbose_name_plural='cursos'

    def __str__(self):
        return self.title
    
