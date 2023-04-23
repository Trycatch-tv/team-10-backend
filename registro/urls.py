from rest_framework import routers
from .api import * 

router = routers.DefaultRouter()

router.register('api/registro',UserViewSet,'registro')
router.register('api/categoria_user',CategoriaViewSet,'categoria_user')

urlpatterns = router.urls