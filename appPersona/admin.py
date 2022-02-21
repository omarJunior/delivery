from django.contrib import admin
from .models import Cliente, Persona


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo',
                    'tipoIdentificacion',
                    'numeroIdentificacion',
                    'nombres',
                    'apellidos',
                    'correo_electronico',
                    'fecha_nacimiento',
                    'edad',
                    'direccion',
                    'telefono',
                    'descuento',
                    'obj_user_referenciado',
                    'sys_active',)
    list_filter = ('codigo', 'nombres', 'apellidos')

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id','obj_user',
                        'tipoIdentificacion',
                        'numeroIdentificacion',
                        'get_full_name_persona',
                        'correo_electronico',
                        'edad',
                        'get_rol_persona',
                        'sys_active',)
    list_filter = ('nombres', 'apellidos', 'correo_electronico', 'rol_persona')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Persona, PersonaAdmin)