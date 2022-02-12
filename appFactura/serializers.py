from rest_framework import serializers
from .models import Factura, Producto, Receta

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}

    
class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}

    