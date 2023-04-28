from django.urls import path, include
from .views import * 




urlpatterns = [
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('auth/signup/',
         SignupView.as_view(), name='auth_signup'),

    path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

     path('groups/', RoleGroupListCreateView.as_view(), name='group-list'),
     path('groups/<int:pk>/', RoleGroupRetrieveUpdateDestroyView.as_view(), name='group-detail'),

     path('users/profesores/',UsuariosAdministradoresAPIView.as_view(), name='profesor'),
     path('users/estudiantes/',UsuariosEstudiantesAPIView.as_view(), name='estudiantes'),

     path('user_info/', UserInfoView.as_view(), name='user_info'),
     path('registrarse_curso/',  RegistroEstudianteView.as_view(), name='registrarse_curso')



    
]
