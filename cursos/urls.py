from rest_framework import routers
from .api import * 


router = routers.DefaultRouter()

router.register('api/cursos',CursoViewSet,'cursos')
router.register('api/categorias',CategoriaViewSet,'categorias')




urlpatterns = router.urls


