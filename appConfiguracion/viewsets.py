from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import (
    TipoIdentificacionSerializer,
    RubroSerializer,
    StockSerializer,
    IngredienteSerializer,
    FormaPagoSerializer,
    PaginationSerializer
)
from .models import TipoIndetificacion, Rubro, Stock, Ingrediente, FormaPago

class TipoIdentificacionViewSet(viewsets.ModelViewSet):
    queryset = TipoIndetificacion.objects.all().order_by('id')
    serializer_class = TipoIdentificacionSerializer
    pagination_class = PaginationSerializer
    permission_classes = (AllowAny,)

class RubroViewSet(viewsets.ModelViewSet):
    queryset = Rubro.objects.all().order_by('id')
    serializer_class = RubroSerializer
    pagination_class = PaginationSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockSerializer
    pagination_class = PaginationSerializer

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all().order_by('id')
    serializer_class = IngredienteSerializer
    pagination_class = PaginationSerializer

class FormaPagoViewSet(viewsets.ModelViewSet):
    queryset = FormaPago.objects.all().order_by('id')
    serializer_class = FormaPagoSerializer
    pagination_class = PaginationSerializer

