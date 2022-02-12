from django.db import models
from appConfiguracion.models import TipoIndetificacion
from django.contrib.auth.models import User, Group

# Create your models here.
class Cliente(models.Model):
    codigo = models.CharField(verbose_name="Codigo del cliente", max_length=55, null=True, blank=True)
    tipoIdentificacion = models.ForeignKey(TipoIndetificacion, verbose_name="Tipo de identificacion", null=True, blank=True, on_delete=models.SET_NULL)
    numeroIdentificacion = models.CharField("Numero de identificacion", max_length=60, null=True, blank=True)
    nombres = models.CharField(verbose_name="Nombres", max_length=100, null=True, blank=True)
    apellidos = models.CharField(verbose_name="Apellidos", max_length=100, null=True, blank=True)
    correo_electronico = models.EmailField(verbose_name= "Email", null=True, blank=True, unique=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento", null=True, blank=True)
    edad = models.IntegerField(verbose_name="Edad", null=True, blank=True)
    direccion = models.CharField(verbose_name="Direccion", max_length=50, null=True, blank=True)
    telefono = models.CharField(verbose_name="Telefono", max_length=50, null=True, blank=True)
    descuento = models.FloatField(verbose_name="Descuento", null=True, blank=True)

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
    obj_user = models.ForeignKey(User, verbose_name="Usuario registrado", null=True, blank=True, on_delete=models.SET_NULL)
    tipoIdentificacion = models.ForeignKey(TipoIndetificacion, verbose_name="Tipo de identificacion", null=True, blank=True, on_delete=models.SET_NULL)
    numeroIdentificacion = models.CharField(verbose_name="Numero de identificacion", max_length=60, null=True, blank=True)
    nombres = models.CharField(verbose_name="Nombres", max_length=100, null=True, blank=True)
    apellidos = models.CharField(verbose_name="Apellidos", max_length=100, null=True, blank=True)
    correo_electronico = models.EmailField(verbose_name="Email", null=True, blank=True, unique=True)
    edad = models.IntegerField(verbose_name="Edad", null=True, blank=True)
    rol_persona = models.ManyToManyField(Group)
    sys_active = models.BooleanField(default=True)

    @property
    def get_full_name_persona(self):
        return self.nombres + " " + self.apellidos

    @property
    def get_rol_persona(self):
        grupos = ""
        grupo = self.obj_user.groups.all()
        if grupo.count() > 0:
            for i in grupo:
                grupos  = grupos + i.name
        return grupos

    sys_fechaCreacion = models.DateTimeField(auto_now_add= True)
    sys_fechaActualizacion = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "appPersonaPersona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.get_rol_persona + " " + self.get_full_name_persona

