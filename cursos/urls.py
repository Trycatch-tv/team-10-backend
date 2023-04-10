from rest_framework import routers
from .api import * 

router = routers.DefaultRouter()

router.register('api/cursos',CursoViewSet,'cursos')
router.register('api/categorias',CategoriaViewSet,'categorias')
router.register('api/estudiantes',EstudianteViewSet,'estudiantes')

urlpatterns = router.urls


