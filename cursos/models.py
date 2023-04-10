from django.db import models

# Create your models here
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Domicilio(models.Model):
    calle=models.CharField(max_length=100)
    altura=models.IntegerField()
    ciudad=models.CharField(max_length=100)
    provincia=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    
    class Meta:
        verbose_name='domicilio'
        verbose_name_plural='domicilios'

    def __str__(self):
        return self.calle,self.altura,self.ciudad,self.pais

class Estudiante(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    dni=models.CharField(max_length=16)
    #imagen=models.ImageField(upload_to='Estudiante', null=True, blank=True)
    telefono=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    domicilio=models.ForeignKey(Domicilio,on_delete=models.CASCADE,null=True)
    created_at=models.TimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    @property
    def cursos_details(self):
        return self.curso.all() 
    
    class Meta:
        verbose_name='estudiante'
        verbose_name_plural='estudiantes'
        
    def __str__(self):
        return self.nombre    
    
class Curso(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    tutor=models.CharField(max_length=200)
    #imagen=models.ImageField(upload_to='Curso', null=True, blank=True)
    estudiante=models.ManyToManyField(Estudiante)
    categoria=models.ManyToManyField(Categoria)
    created_at=models.TimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='curso'
        verbose_name_plural='cursos'

    def __str__(self):
        return self.title