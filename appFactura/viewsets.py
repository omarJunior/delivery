from django.http.response import HttpResponse
from rest_framework import viewsets, status, exceptions
from rest_framework.decorators import action
from appPersona.models import Cliente
from appConfiguracion.models import FormaPago, Rubro, Stock

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

    @action(detail = False, methods=['post'], url_path="registro-factura", url_name="registro_factura")
    def registro_factura(self, request):
        nro_comprobante = request.data['nro_comprobante']
        fecha = request.data['fecha']
        id_cliente = request.data['id_cliente']
        id_forma_pago = request.data['id_forma_pago']
        iva = request.data['iva']
        descuento = request.data['descuento']
        factura_obj = Factura()
        factura_obj.nro_comprobante = nro_comprobante
        factura_obj.fecha = fecha
        factura_obj.obj_cliente = Cliente()
        factura_obj.obj_cliente.id = id_cliente
        factura_obj.obj_forma_pago = FormaPago()
        factura_obj.obj_forma_pago.id = id_forma_pago
        factura_obj.iva = iva
        factura_obj.descuento = descuento
        factura_obj.save()

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer

    @action(detail=False, methods=['post'], url_path="register-producto", url_name="register_producto")
    def register_producto(self, request):
        descripcion = request.data['descripcion']
        costo = request.data['costo']
        precio_final = request.data['precio_final']
        id_rubro = request.data['id_rubro']
        id_stock = request.data['id_stock']
        tamanio = request.data['tamanio']

        try:
            precio_sin_iva = request.data['precio_sin_iva']
        except:
            precio_sin_iva = None

        producto = Producto()
        producto.descripcion = descripcion
        producto.costo = costo
        producto.precio_final = precio_final
        if precio_sin_iva is not None:
            producto.precio_sin_iva = precio_sin_iva
            
        producto.obj_rubro = Rubro()
        producto.obj_rubro.id = id_rubro
        producto.obj_stock = Stock()
        producto.obj_stock.id = id_stock
        producto.tamanio = tamanio
        producto.save()

    

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('id')
    serializer_class = RecetaSerializer