from rest_framework import serializers
from .models import TipoIndetificacion, Rubro, Stock, Ingrediente, FormaPago
from rest_framework import pagination

class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 50

class TipoIdentificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIndetificacion
        fields = ('__all__')

class RubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubro
        fields = ('__all__')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('__all__')

class IngredienteSerializer(serializers.ModelSerializer):
    obj_stock = StockSerializer(many=False, read_only= True)

    class Meta:
        model = Ingrediente
        fields = [
            'id',
            'descripcion',
            'cantidad',
            'unidad_medida',
            'costo',
            'obj_stock'
        ]

class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = ('__all__')

    