import utils
from django.db import models
from appPersona.models import Cliente
from appConfiguracion.models import FormaPago, Rubro, Stock, Ingrediente


# Create your models here.
class Factura(models.Model):
    nro_comprobante = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(auto_now=True,null=True, blank=True)
    obj_cliente = models.ForeignKey(Cliente, verbose_name="Cliente", null=True, blank=True, on_delete=models.SET_NULL)
    obj_forma_pago = models.ForeignKey(FormaPago, verbose_name="Forma de pago", null=True, blank=True, on_delete=models.SET_NULL)
    iva = models.FloatField(null=True, blank=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appFacturaFactura"
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return self.nro_comprobante +  " " + self.obj_cliente

class Producto(models.Model):
    descripcion = models.CharField(max_length=80, null=True, blank=True)
    costo = models.FloatField(null=True, blank=True)
    precio_sin_iva = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    obj_rubro = models.ForeignKey(Rubro, verbose_name="Rubro", null=True, blank=True, on_delete=models.SET_NULL)
    obj_stock = models.ForeignKey(Stock, verbose_name="Stock", null=True, blank=True, on_delete=models.SET_NULL)
    tamanio = models.CharField(max_length=60, choices=utils.TAMANIO_PRODUCTO)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "appFacturaProducto"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.descripcion +  " " + str(self.costo)


class Receta(models.Model):
    obj_ingrediente = models.ForeignKey(Ingrediente, verbose_name="Ingrediente", null=True, blank=True, on_delete=models.SET_NULL)
    obj_producto = models.ForeignKey(Producto, verbose_name="Producto", null=True, blank=True, on_delete=models.SET_NULL)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appFacturaReceta"
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"

    def __str__(self):
        return self.obj_ingrediente + " " + self.obj_producto
