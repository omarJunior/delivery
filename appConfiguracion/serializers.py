from rest_framework import serializers
from .models import TipoIndetificacion, Rubro, Stock, Ingrediente, FormaPago

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
    obj_stock = serializers.SerializerMethodField(method_name="get_stock")

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
        read_only_fields = ('obj_stock',) 

    def get_stock(self, obj):
        if obj.obj_stock:
            return f"Stock Maximo {obj.obj_stock.stock}, Stock Minimo {obj.obj_stock.stock_minimo}" 
        return ""

class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = ('__all__')

    