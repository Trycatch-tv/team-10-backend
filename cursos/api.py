from .models import *
from rest_framework import viewsets, permissions
#from rest_auth.registration.views import RegisterView
from .serializers import *

#class CustomRegisterView(RegisterView):
    #pass

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer
    

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = EstudianteSerializer    
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset=Curso.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = CursoSerializer        