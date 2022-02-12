import utils
from django.db import models

# Create your models here.
class TipoIndetificacion(models.Model):
    sigla = models.CharField(verbose_name="Sigla", max_length=50, null=True, blank=True)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=70, null=True, blank=True)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)
    
    class Meta: 
        db_table = "appConfiguracionTipoIdentificacion"
        verbose_name = "Tipo de identificacion"
        verbose_name_plural = "Tipos de indentificaciones"

    def __str__(self):
        return self.descripcion

class Rubro(models.Model):
    descripcion = models.CharField(verbose_name="Descripcion del rubro", max_length=80, null=True, blank=True)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appConfiguracionRubro"
        verbose_name = "Rubro"
        verbose_name_plural = "Rubros"

    def __str__(self):
        return self.descripcion

class Stock(models.Model):
    stock = models.CharField(verbose_name="Stock", max_length=55, null=True, blank=True)
    stock_minimo = models.CharField(verbose_name="Stock minimo", max_length=100, null=True, blank=True)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appConfiguracionStock"
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return f"Stock maximo: {self.stock} Stock minimo = {self.stock_minimo}"

class Ingrediente(models.Model):
    descripcion = models.CharField(verbose_name="Descripcion", max_length=55, null=True, blank=True)
    cantidad = models.IntegerField(verbose_name="Cantidad", null=True, blank=True)
    unidad_medida = models.CharField(verbose_name="Unidad medida", max_length=30, null=True, blank=True)
    costo = models.FloatField(verbose_name="Costo", null=True, blank=True)
    obj_stock = models.ForeignKey(Stock, verbose_name="Stock", null=True, blank=True, on_delete=models.SET_NULL)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appConfiguracionIngrediente"
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return self.descripcion + " Cantidad: " + str(self.cantidad)

class FormaPago(models.Model):
    nombre = models.CharField(verbose_name="Tipo de pago", max_length=100, choices= utils.FORMA_DE_PAGOS, null=True, blank=True)
    otros_detalles = models.CharField(verbose_name="Detalles", max_length=55, null=True, blank=True)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appConfiguracionFormaPago"
        verbose_name = "Forma de pago"
        verbose_name_plural = "Forma de pagos"

    def __str__(self):
        return self.nombre