from rest_framework import viewsets
from .serializers import (
    TipoIdentificacionSerializer,
    RubroSerializer,
    StockSerializer,
    IngredienteSerializer,
    FormaPagoSerializer,
)
from .models import TipoIndetificacion, Rubro, Stock, Ingrediente, FormaPago

class TipoIdentificacionViewSet(viewsets.ModelViewSet):
    queryset = TipoIndetificacion.objects.all().order_by('id')
    serializer_class = TipoIdentificacionSerializer

class RubroViewSet(viewsets.ModelViewSet):
    queryset = Rubro.objects.all().order_by('id')
    serializer_class = RubroSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockSerializer

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all().order_by('id')
    serializer_class = IngredienteSerializer

class FormaPagoViewSet(viewsets.ModelViewSet):
    queryset = FormaPago.objects.all().order_by('id')
    serializer_class = FormaPagoSerializer

