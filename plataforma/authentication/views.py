from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserLogin
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from .mail import correo
from .models import RoleGroup
from .serializers import RoleGroupSerializer, CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsStudent, IsAdmin
from django.contrib.auth.models import Group
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from cursos.models import *
from cursos.api import RegistrarseCursoViewSet





# formato { "email": "", "password": "" }

class LoginView(APIView):
    serializer_class = UserLogin

    def post(self, request):
        # Si el usuario ya tiene una sesión abierta, cerrarla
        #if request.user.is_authenticated:
           #logout(request)

        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        groupAdmin = Group.objects.get(name='profesor')
        groupEstudiante = Group.objects.get(name='estudiante')

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            print(UserSerializer(user).data['rol'])
            if UserSerializer(user).data['rol'] == 'profesor':
                print("El usuario es profesor") 
            elif UserSerializer(user).data['rol'] == 'estudiante':
                print("El usuario es estudiante") 
            elif UserSerializer(user).data['rol'] != '':
                print("El usuario es : ", UserSerializer(user).data['rol'] ) 
            return Response(
                    UserSerializer(user).data, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response({'detail': '{"email":"youremail@mail.com", "password": "12345678" }'}, status=status.HTTP_404_NOT_FOUND)

        

class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)


class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        # Verificar si ya existe un usuario con el mismo correo electrónico
        if CustomUser.objects.filter(email=email).exists():
            return Response({'detail': 'Ya existe un usuario con este correo electrónico.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().create(request, *args, **kwargs)
   

    
#@permission_classes([IsAdmin])
class RoleGroupListCreateView(generics.ListCreateAPIView):
    queryset = RoleGroup.objects.all()
    serializer_class = RoleGroupSerializer

#@permission_classes([IsAdmin])
class RoleGroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoleGroup.objects.all()
    serializer_class = RoleGroupSerializer
   

#@permission_classes([IsAdmin])
class UsuariosAdministradoresAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        User = get_user_model()
        queryset = User.objects.filter(rol='profesor')
        return queryset
    
#@permission_classes([IsAdmin])
class UsuariosEstudiantesAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        User = get_user_model()
        queryset = User.objects.filter(rol='estudiante')
        return queryset
  

        
class UserInfoView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            # Si el usuario está autenticado, devolvemos su información
            user_data = UserSerializer(request.user).data
            return Response(user_data)
        #else:
            # Si el usuario no está autenticado, devolvemos un error
            #return Response({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)
        
"""class RegistrarseCursoView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            # Se crea una nueva instancia de RegistrarseCurso
            registrarse_curso = RegistrarseCursoViewSet()

            # Se establece el nombre del estudiante como el nombre del usuario autenticado
            registrarse_curso.estudiante = UserInfoView
            estudiante = registrarse_curso.estudiante
            print(estudiante)


            # Se obtiene la instancia del curso correspondiente al ID
            curso = registrarse_curso.nombre('nombre')

            # Se añade el curso a la lista de cursos relacionados con el registro del estudiante
            registrarse_curso.nombre.add(curso)
            registrarse_curso.estudiante.add(estudiante)


            # Se guarda la instancia de RegistrarseCurso en la base de datos
            registrarse_curso.save()

            return Response({"mensaje": "El estudiante se ha registrado correctamente en el curso."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)"""




receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Aquí deberíamos mandar un correo al cliente...
     print(
        f"\nRecupera la contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API http://localhost:8000/api/auth/reset/confirm/.")
     correo([reset_password_token.user.email])
     




