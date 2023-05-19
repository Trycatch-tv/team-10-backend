from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserLogin
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from .mail import correo
from .permissions import *
from .models import CustomUser
from cursos.models import *


# login



class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        # Verificar si ya existe un usuario con el mismo correo electrónico
        if CustomUser.objects.filter(email=email).exists():
            return Response({'detail': 'Ya existe un usuario con este correo electrónico.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().create(request, *args, **kwargs)
        


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

        
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            print(UserSerializer(user).data['id'])
            print(UserSerializer(user).data['username'])
            print(UserSerializer(user).data['rol'])
            return Response(
                UserSerializer(user).data['username'], status=status.HTTP_200_OK)
                    #UserSerializer(user).data, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response({'detail': '{"email":"youremail@mail.com", "password": "12345678" }'}, status=status.HTTP_404_NOT_FOUND)

        
class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response({'detail': 'Logout exitoso'},status=status.HTTP_200_OK)



   
receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Aquí deberíamos mandar un correo al cliente...
     print(
        f"\nRecupera la contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API http://localhost:8000/api/auth/reset/confirm/.")
     correo([reset_password_token.user.email])








