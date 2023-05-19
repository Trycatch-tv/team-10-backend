from django.urls import path, include
from .views import * 


urlpatterns = [
    path('groups/', RoleGroupListCreateView.as_view(), name='group-list'),
    path('groups/<int:pk>/', RoleGroupRetrieveUpdateDestroyView.as_view(), name='group-detail'),
    path('users/administradores/',UsuariosAdministradoresAPIView.as_view(), name='administradores'),
    path('users/profesores/',UsuariosProfesoresAPIView.as_view(), name='profesores'),
    path('users/profesores/<int:pk>/',UsuariosProfesoresRolEdit.as_view(), name='profesores-edit-rol'),
    path('users/estudiantes/',UsuariosEstudiantesAPIView.as_view(), name='estudiantes'),
    path('users/estudiantes/<int:pk>/',UsuariosEstudiantesRolEdit.as_view(), name='estudiantes-edit-rol'),
    path('users/edit/',UsuariosEdit.as_view(), name='users-edit'),
    path('user_info/', UserInfoView.as_view(), name='user_info')
    #path('registrarse_curso/',  RegistroEstudianteView.as_view(), name='registrarse_curso')
]