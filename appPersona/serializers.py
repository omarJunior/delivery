from rest_framework import serializers
from .models import Cliente, Persona

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('__all__')
        extra_kwargs = {'id': {'required': True}}
