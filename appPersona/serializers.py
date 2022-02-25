from rest_framework import serializers
from .models import Cliente, Persona, User


class UserSerializers(serializers.ModelSerializer):
    grupo = serializers.SerializerMethodField(method_name="get_name_grupo")
    tipoIdentificacion = serializers.SerializerMethodField(method_name = "get_tipo_identificacion")
    numeroIdentificacion = serializers.SerializerMethodField(method_name = "get_numero_identificacion")
    edad = serializers.SerializerMethodField(method_name = "get_edad")
    direccion = serializers.SerializerMethodField(method_name = "get_direccion")
    ciudad = serializers.SerializerMethodField(method_name="get_ciudad")
    telefono = serializers.SerializerMethodField(method_name = "get_telefono")
    codigo_postal = serializers.SerializerMethodField(method_name="get_codigo_postal")
    descripcion = serializers.SerializerMethodField(method_name="get_descripcion")

    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'grupo',
            'tipoIdentificacion',
            'numeroIdentificacion',
            'edad',
            'direccion',
            'ciudad',
            'telefono',
            'codigo_postal',
            'descripcion',
        ]

        read_only_fields = ('grupo', 'tipoIdentificacion', 'numeroIdentificacion', 'edad', 'direccion', 'ciudad' 'telefono', 'codigo_postal', 'descripcion')


    def get_name_grupo(self, obj):
        name=""
        if obj.groups:
            for i in obj.groups.all():
                name = name + i.name
        return name
        
    def get_tipo_identificacion(self, obj):
        if obj.user_persona:
            for i in obj.user_persona.all():
                return i.tipoIdentificacion.descripcion
        return ""

    def get_numero_identificacion(self, obj):
        if obj.user_persona:
            for i in obj.user_persona.all():
                return i.numeroIdentificacion
        return ""

    def get_edad(self, obj):
        if obj.user_persona:
            for i in obj.user_persona.all():
                return i.edad
        return ""

    def get_direccion(self, obj):
        if obj.user_persona:
            for i in obj.user_persona.all():
                return i.direccion
        return ""
    
    def get_ciudad(self, obj):
        if obj.user_persona:
            for i in obj.user_persona.all():
                return i.ciudad
        return ""

    def get_telefono(self, obj):
        if obj.user_persona:
            for i in obj.user_persona.all():
                return i.telefono
        return "" 

    def get_codigo_postal(self, obj):
        if obj.user_persona:
            for i in obj.user_persona.all():
                return i.codigo_postal
        return ""

    def get_descripcion(self, obj):
        if obj.user_persona:
            for i in obj.user_persona.all():
                return i.descripcion
        return ""

class ClienteSerializer(serializers.ModelSerializer):
    tipoIdentificacion = serializers.CharField(source = "tipoIdentificacion.descripcion")
    obj_user_referenciado = serializers.SerializerMethodField(method_name = "get_full_name")
    
    class Meta:
        model = Cliente
        fields = [
            'id',
            'codigo',
            'tipoIdentificacion',
            'numeroIdentificacion',
            'nombres',
            'apellidos',
            'correo_electronico',
            'fecha_nacimiento',
            'edad',
            'direccion',
            'ciudad',
            'telefono',
            'descuento',
            'obj_user_referenciado',
        ]

        read_only_fields = ('tipoIdentificacion', 'obj_user_referenciado',) 
    
    def get_full_name(self, obj):
        if obj.obj_user_referenciado:
            return obj.obj_user_referenciado.get_full_name()
        return ""
        
class PersonaSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name="get_full_name")
    username = serializers.SerializerMethodField(method_name="get_user_name")
    tipoIdentificacion = serializers.CharField(source = "tipoIdentificacion.descripcion")
    obj_user = UserSerializers(many=False)

    class Meta:
        model = Persona
        fields = [
            'id',
            'obj_user',
            'full_name',
            'username',
            'tipoIdentificacion',
            'numeroIdentificacion',
            'nombres',
            'apellidos',
            'correo_electronico',
            'edad',
            'direccion',
            'ciudad',
            'telefono',
            'codigo_postal',
            'descripcion',
            'get_rol_persona',
        ]
        read_only_fields = ('tipoIdentificacion', 'obj_user',) 

    def get_full_name(self, obj):
        if obj.obj_user:
            return obj.obj_user.get_full_name()
        return ""

    def get_user_name(self, obj):
        if obj.obj_user:
            return obj.obj_user.username
        return ""

        