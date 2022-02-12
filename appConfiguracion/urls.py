from rest_framework.routers import DefaultRouter

#Viewsets de las app
from .viewsets import (
    TipoIdentificacionViewSet,
    RubroViewSet,
    StockViewSet,
    IngredienteViewSet,
    FormaPagoViewSet,
)

router = DefaultRouter()
router.register(r"tipo-identificacion", TipoIdentificacionViewSet)
router.register(r"rubro", RubroViewSet)
router.register(r"stock", StockViewSet)
router.register(r"ingredientes", IngredienteViewSet)
router.register(r"forma-pago", FormaPagoViewSet)