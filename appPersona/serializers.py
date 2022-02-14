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
    obj_user = serializers.SerializerMethodField(method_name="get_full_name")
    tipoIdentificacion = serializers.CharField(source = "tipoIdentificacion.descripcion")

    class Meta:
        model = Persona
        fields = [
            'id',
            'obj_user',
            'tipoIdentificacion',
            'numeroIdentificacion',
            'nombres',
            'apellidos',
            'correo_electronico',
            'edad',
            'get_rol_persona',
        ]
        read_only_fields = ('tipoIdentificacion', 'obj_user',) 

    def get_full_name(self, obj):
        if obj.obj_user:
            return obj.obj_user.get_full_name()
        return ""

