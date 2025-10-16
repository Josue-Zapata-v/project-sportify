from rest_framework.routers import DefaultRouter
from .views import EquipoViewSet, JugadorViewSet

router = DefaultRouter()
router.register(r'equipos', EquipoViewSet, basename='equipo')
router.register(r'jugadores', JugadorViewSet, basename='jugador')

urlpatterns = router.urls
