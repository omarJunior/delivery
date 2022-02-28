from django.contrib import admin
from .models import Factura, Producto, Receta


# Register your models here.
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nro_comprobante', 'fecha', 'obj_cliente', 'obj_forma_pago', 'iva', 'descuento', 'total', 'sys_active',)
    list_filter = ('nro_comprobante', 'obj_cliente',) 

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'costo', 'precio_sin_iva', 'precio_final', 'obj_rubro', 'tamanio', 'sys_active',)
    list_filter = ('descripcion', 'costo',)

class RecetaAdmin(admin.ModelAdmin):
    list_display = ('obj_ingrediente', 'obj_producto', 'sys_active', )
    list_filter = ('obj_producto',)

admin.site.register(Factura, FacturaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Receta, RecetaAdmin)