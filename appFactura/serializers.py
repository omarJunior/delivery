from rest_framework import serializers
from .models import Factura, Producto, Receta
from rest_framework import pagination

class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100

class FacturaSerializer(serializers.ModelSerializer):
    obj_cliente = serializers.SerializerMethodField(method_name="get_full_name")
    obj_forma_pago = serializers.CharField(source = "obj_forma_pago.nombre")

    class Meta:
        model = Factura
        fields = [
            'id',
            'nro_comprobante',
            'fecha',
            'obj_cliente',
            'obj_forma_pago',
            'iva',
            'descuento',
            'total'
            
        ]
        read_only_fields = ('obj_cliente', 'obj_forma_pago',)

    def get_full_name(self, obj):
        if obj.obj_cliente:
            return obj.obj_cliente.get_full_name
        return ""
        

class ProductoSerializer(serializers.ModelSerializer):
    obj_rubro = serializers.CharField(source = "obj_rubro.descripcion")
    obj_stock = serializers.CharField(source = "obj_stock.stock")

    class Meta:
        model = Producto
        fields = [
            'id',
            'descripcion',
            'costo',
            'precio_sin_iva',
            'precio_final',
            'obj_rubro',
            'obj_stock',
            'tamanio'
        ]
        read_only_fields = ('obj_rubro', 'obj_stock')
    
class RecetaSerializer(serializers.ModelSerializer):
    obj_ingrediente = serializers.CharField(source = "obj_ingrediente.descripcion")
    obj_producto = serializers.SerializerMethodField(method_name="get_producto")
    
    class Meta:
        model = Receta
        fields = [
            'id',
            'obj_ingrediente',
            'obj_producto'
        ]
        read_only_fields = ('obj_ingrediente', 'obj_producto',)

    def get_producto(self, obj):
        if obj.obj_producto:
            return obj.obj_producto.descripcion
        return ""


    