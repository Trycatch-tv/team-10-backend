from rest_framework import routers
from .api import * 


router = routers.DefaultRouter()

router.register('api/curso',CursoViewSet,'curso')
router.register('api/cursos',CursoList,'cursos')
router.register('api/categorias',CategoriaViewSet,'categorias')
#router.register('api/registrarse_curso',RegistrarseCursoViewSet,'registrarse_curso')




urlpatterns = router.urls


