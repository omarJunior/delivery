from django.db import models
from appConfiguracion.models import TipoIndetificacion
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    codigo = models.CharField(max_length=55, null=True, blank=True)
    tipoIdentificacion = models.ForeignKey(TipoIndetificacion, null=True, blank=True, on_delete=models.SET_NULL)
    numeroIdentificacion = models.CharField(max_length=60, null=True, blank=True)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    descuento = models.FloatField(null=True, blank=True)

    @property
    def get_full_name(self):
        return self.nombres + " " + self.apellidos

    sys_active = models.BooleanField(default=True)
    sys_fechaCreacion = models.DateTimeField(auto_now_add= True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appPersonaCliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.codigo + " " + self.get_full_name()

#Hacer referencia al auth user
class Persona(models.Model):
    obj_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    tipoIdentificacion = models.ForeignKey(TipoIndetificacion, null=True, blank=True, on_delete=models.SET_NULL)
    numeroIdentificacion = models.CharField(max_length=60, null=True, blank=True)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True, unique=True)
    edad = models.IntegerField(null=True, blank=True)
    rol_persona = models.CharField(max_length=60, null=True, blank=True)
    sys_active = models.BooleanField(default=True)

    @property
    def get_full_name_persona(self):
        return self.nombres + " " + self.apellidos

    sys_fechaCreacion = models.DateTimeField(auto_now_add= True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appPersonaPersona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.rol_persona + " " + self.get_full_name_persona()

