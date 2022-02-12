from django.contrib import admin
from .models import TipoIndetificacion, Rubro, Stock, Ingrediente, FormaPago

# Register your models here.
class TipoIdentificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sigla', 'descripcion', 'sys_active',)
    list_filter = ('sigla', 'descripcion',)

class RubroAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'sys_active')
    list_filter = ('descripcion',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock', 'stock_minimo', 'sys_active',)
    list_filter = ('stock',)

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'cantidad', 'unidad_medida', 'costo', 'obj_stock', 'sys_active',) 
    list_filter = ('descripcion', 'cantidad',)

class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'otros_detalles', 'sys_active',)
    list_filter = ('nombre',)

admin.site.register(TipoIndetificacion, TipoIdentificacionAdmin)
admin.site.register(Rubro, RubroAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(FormaPago, FormaPagoAdmin)
