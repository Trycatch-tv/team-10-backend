from django.urls import path
from .views import CursoList, CursoDetail, EstudianteList, EstudianteDetail


# endpoints de API

urlpatterns = [
    path('cursos/', CursoList.as_view(), name='cursos-list'),
    path('cursos/<int:pk>/', CursoDetail.as_view(), name='cursos-detail'),

    path('estudiantes/', EstudianteList.as_view(), name='estudiante-list'),
    path('estudiantes/<int:pk>/', EstudianteDetail.as_view(), name='estudiante-detail'),

]