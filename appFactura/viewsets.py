from django.http.response import HttpResponse
from rest_framework import viewsets, status, exceptions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
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
    queryset = Factura.objects.filter(sys_active = True).order_by('id')
    serializer_class = FacturaSerializer

    #cantidad de facturas que existen
    @action(detail=False, methods=['get'], url_path="get_factura", url_name="get-factura")
    def get_factura(self, request):
        facturas = Factura.objects.filter(sys_active = True).count()
        return Response({'facturas': facturas})

    @action(detail = False, methods=['post'], url_path="register_factura", url_name="register-factura")
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

    #total money factura
    @action(detail=False, methods=['get'], url_path="get_total", url_name="get-total")
    def get_total(self, request):
        facturas = Factura.objects.all().values('id', 'total')
        contador = 0
        for i in facturas:
            contador = contador + i['total']
        return Response({'total_money_factura': contador})


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.filter(sys_active = True).order_by('id')
    serializer_class = ProductoSerializer

    #cantidad de productos que existen
    @action(detail=False, methods=['get'], url_path="get_productos", name="get-productos")
    def get_productos(self, request):
        productos = Producto.objects.filter(sys_active = True).count()
        return Response({'productos': productos})

    @action(detail=False, methods=['post'], url_path="register_producto", url_name="register-producto")
    def register_producto(self, request):
        try:
            descripcion = request.data['descripcion']
        except:
            descripcion = None
        try:
            costo = request.data['costo'] 
        except:
            costo = None
        try:
            precio_sin_iva = request.data['precio_sin_iva']
        except:
            precio_sin_iva = None
        try:
            precio_final = request.data['precio_final']
        except:
            precio_final = None
        try:
            id_rubro = request.data['id_rubro']
        except:
            id_rubro = None
        try:
            id_stock = request.data['id_stock']
        except:
            id_stock = None
        try:
            tamanio = request.data['tamanio']
        except:
            tamanio = None
       
        producto = Producto()
        if descripcion is not None:
            producto.descripcion = descripcion
        if costo is not None:
            producto.costo = costo
        if precio_final is not None:
            producto.precio_final = precio_final
        if precio_sin_iva is not None:
            producto.precio_sin_iva = precio_sin_iva
        if id_rubro is not None:
            producto.obj_rubro = Rubro()
            producto.obj_rubro.id = id_rubro
        if id_stock is not None:
            producto.obj_stock = Stock()
            producto.obj_stock.id = id_stock
        if tamanio is not None:
            producto.tamanio = tamanio
        producto.save()
        return Response({'msg': 'Datos guardados correctamente'})

    #total costo de los productos
    @action(detail=False, methods=['get'], url_path="get_total_costo", url_name="get-total-costo")
    def get_total_costo(self, request):
        productos = Producto.objects.all().values('id', 'costo')
        contador = 0
        for i in productos:
            contador = contador + i['costo']
        return Response({'total_costo_producto': contador})


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('id')
    serializer_class = RecetaSerializer