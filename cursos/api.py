from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer
    
class DomicilioViewSet(viewsets.ModelViewSet):
    queryset=Domicilio.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = DomicilioSerializer
    
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = EstudianteSerializer    
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset=Curso.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = CursoSerializer        