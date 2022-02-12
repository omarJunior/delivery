from rest_framework import serializers
from .models import TipoIndetificacion, Rubro, Stock, Ingrediente, FormaPago

class TipoIdentificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIndetificacion
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}

class RubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubro
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}

class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}
    