from rest_framework.routers import DefaultRouter
from .viewsets import ClienteViewSet, PersonaViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'persona', PersonaViewSet)