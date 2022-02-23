from rest_framework import serializers
from .models import Cliente, Persona

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

    class Meta:
        model = Persona
        fields = [
            'id',
            'full_name',
            'username',
            'tipoIdentificacion',
            'numeroIdentificacion',
            'nombres',
            'apellidos',
            'correo_electronico',
            'edad',
            'direccion',
            'telefono',
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

