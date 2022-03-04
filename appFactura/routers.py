from rest_framework.routers import DefaultRouter

from .viewsets import (
    FacturaViewSet,
    ProductoViewSet,
    RecetaViewSet,
)

router = DefaultRouter()
router.register(r'factura', FacturaViewSet)
router.register(r'producto', ProductoViewSet)
router.register(r'receta', RecetaViewSet)

urlpatterns = router.urls