from rest_framework import viewsets

from .models import (
    Factura,
    Producto,
    Receta
)
from .serializers import (
    FacturaSerializer,
    ProductoSerializer,
    RecetaSerializer,
)

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all().order_by('id')
    serializer_class = FacturaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('id')
    serializer_class = RecetaSerializer