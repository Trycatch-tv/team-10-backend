from .models import *
from rest_framework import viewsets, permissions
#from rolepermissions.decorators import role_required
from .serializers import *

#class CustomRegisterView(RegisterView):
    #pass

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer
    


#@role_required('administrador')
class CursoViewSet(viewsets.ModelViewSet):
    queryset=Curso.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = CursoSerializer        