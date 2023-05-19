from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from authentication.permissions import IsAdmin
from rest_framework.response import Response
from rest_framework import status



@permission_classes([IsAdmin])
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer
    

@permission_classes([IsAdmin])
class CursoViewSet(viewsets.ModelViewSet):
    queryset=Curso.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = CursoSerializer        


class CursoList(viewsets.ReadOnlyModelViewSet):
    queryset = Curso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursoSerializer




"""class RegistrarseCursoViewSet(viewsets.ModelViewSet, APIView):
    queryset=RegistrarseCurso.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = RegistrarseCursoSerializer  """
    

