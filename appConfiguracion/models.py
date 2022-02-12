import utils
from django.db import models

# Create your models here.
class TipoIndetificacion(models.Model):
    sigla = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.CharField(max_length=70, null=True, blank=True)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)
    
    class Meta: 
        db_table = "appConfiguracionTipoIdentificacion"
        verbose_name = "Tipo de identificacion"
        verbose_name = "Tipos de indentificaciones"

    def __str__(self):
        return self.descripcion

class Rubro(models.Model):
    descripcion = models.CharField(max_length=80, null=True, blank=True)
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
    stock = models.CharField(max_length=55, null=True, blank=True)
    stock_minimo = models.CharField(max_length=100, null=True, blank=True)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appConfiguracionStock"
        verbose_name = "Stock"
        verbose_name = "Stocks"

    def __str__(self):
        return f"Stock maximo: {self.stock} Stock minimo = {self.stock_minimo}"

class Ingrediente(models.Model):
    descripcion = models.CharField(max_length=55, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    unidad_medida = models.CharField(max_length=30, null=True, blank=True)
    costo = models.FloatField(null=True, blank=True)
    obj_stock = models.ForeignKey(Stock, null=True, blank=True, on_delete=models.SET_NULL)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appConfiguracionIngredientes"
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return self.descripcion + " Cantidad: " + str(self.cantidad)

class FormaPago(models.Model):
    nombre = models.CharField(max_length=100, choices= utils.FORMA_DE_PAGOS, null=True, blank=True)
    otros_detalles = models.CharField(max_length=55, null=True, blank=True)
    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add=True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appConfiguracionFormaPago"
        verbose_name = "Forma de pago"
        verbose_name_plural = "Forma de pagos"

    def __str__(self):
        return self.nombre