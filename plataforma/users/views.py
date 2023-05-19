
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserLogin
from .models import RoleGroup
from .serializers import RoleGroupSerializer, CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from .permissions import *
from .models import CustomUser
from django.contrib.auth import get_user_model
from cursos.models import *
from cursos.models import Curso
from cursos.serializers import CursoSerializer


    
@permission_classes([IsAdmin])
class RoleGroupListCreateView(generics.ListCreateAPIView):
    queryset = RoleGroup.objects.all()
    serializer_class = RoleGroupSerializer

@permission_classes([IsAdmin])
class RoleGroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoleGroup.objects.all()
    serializer_class = RoleGroupSerializer
   
@permission_classes([IsAdmin])
class UsuariosAdministradoresAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        User = get_user_model()
        queryset = User.objects.filter(rol='administrador')
        return queryset
    

#@permission_classes([IsAdmin])
class UsuariosProfesoresAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        User = get_user_model()
        queryset = User.objects.filter(rol='profesor')
        return queryset
    
@permission_classes([IsAdmin])
class UsuariosProfesoresRolEdit(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.filter(rol='profesor')
    #permission_classes = [IsAuthenticated]

    def get_object(self):
        User = get_user_model()
        user_id = self.kwargs['pk']  # Obtiene el ID del usuario de la URL
        return User.objects.get(id=user_id)

#@permission_classes([IsAdmin])
class UsuariosEstudiantesAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        User = get_user_model()
        queryset = User.objects.filter(rol='estudiante')
        return queryset

@permission_classes([IsAdmin])
class UsuariosEstudiantesRolEdit(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.filter(rol='estudiantes')
    #permission_classes = [IsAuthenticated]

    def get_object(self):
        User = get_user_model()
        user_id = self.kwargs['pk']  # Obtiene el ID del usuario de la URL
        return User.objects.get(id=user_id)


        
class UserInfoView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            # Si el usuario está autenticado, devolvemos su información
            user_data = UserSerializer(request.user).data
            return Response(user_data)
        else:
            # Si el usuario no está autenticado, devolvemos un error
            return Response({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

""" en la peticion PATCH solo se pueden incluir los items :
    
    "username": "",
    "cedula": null,
    "email": "",
    "phone": null,
    "password": "",
   
}  
"""

#@permission_classes([IsAdmin])
class UsuariosEdit(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.request.user.id

        User = get_user_model()
        try:
            return User.objects.only('username', 'cedula', 'email', 'phone', 'password').get(id=user_id)
        except User.DoesNotExist:
            raise Response({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # No permitir cambios en los campos 'id' y 'rol'
        if 'id' in request.data or 'rol' in request.data:
            return Response({"error": "No se pueden cambiar los items 'id' o 'rol'"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

       
class RegistroEstudianteView(generics.CreateAPIView):
    serializer_class = CursoSerializer

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Obtiene el usuario autenticado en la sesión
        usuario = UserSerializer(request.user).data

        # Obtiene el id del curso de los parámetros de la solicitud POST
        curso_id = request.data.get('nombre')

        # Obtiene el curso correspondiente al id
        curso = Curso.objects.get(pk=curso_id)

        # Agrega al usuario al curso
        curso.usuarios.add(CustomUser)

        return Response({'message': f'El usuario {usuario.username} ha sido registrado en el curso {curso.nombre}.'})



     





