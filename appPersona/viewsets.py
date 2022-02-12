from asyncio import exceptions
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import viewsets, status, exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cliente, Persona
from .serializers import ClienteSerializer, PersonaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all().order_by('id')
    serializer_class = PersonaSerializer

    @action(detail=False, methods=['post'], url_path="registro")
    def registro(self, request):
        #xd
        pass

class ApiCustomAuthToken(APIView):
    #Permita ingresar a esta vista sin necesidad de estar autenticado
    permission_classes = (AllowAny, )

    def post(self, request, format = None):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            raise exceptions.AuthenticationFailed("Se debe enviar un nombre de usuario y contraseña válido")
        
        user = authenticate(
            username = username,
            password = password
        )
        if user is not None:
            if user.is_active:
                #generamos el token
                refresh = RefreshToken.for_user(user)
                persona = Persona.objects.filter(obj_user = user.pk).values('id', 'tipoIdentificacion', 'numeroIdentificacion').first()
                try:
                    id_persona = persona.get('id')
                except:
                    id_persona = ""
                try:
                    tipo_identificacion = persona.get('tipoIndentificacion')
                except:
                    tipo_identificacion = ""
                try:
                    nro_indentificacion = persona.get('numeroIdentificacion')
                except:
                    nro_indentificacion = ""

                userDict = {
                    "id": user.pk,
                    "id_persona": id_persona,
                    "username": user.username,
                    "correo_electronico": user.email,
                    "fullname": user.get_full_name(),
                    "tipo_identificacion": tipo_identificacion,
                    "nro_identificacion": nro_indentificacion,
                    "roles": [rol.name for rol in user.groups.all()],
                    "refresh": str(refresh),
                    "access_token": str(refresh.access_token)
                }
                return Response(userDict, status=status.HTTP_200_OK)
            else:
                raise exceptions.AuthenticationFailed("El usuario no se encuentra activo")
        else:
            raise exceptions.AuthenticationFailed("Verifique su usuario y contraseña")

    def get(self, request, format=None):
        if request.user.is_authenticated:
            persona = Persona.objects.filter(obj_user = request.user.pk).values('id').first()
            try:
                id_persona = persona.get('id')
            except:
                id_persona = ""
            userDict = {
                "id": request.user.pk,
                "id_persona": id_persona,
                "username": request.user.username,
                "fullname": request.user.get_full_name(),
                "roles": [rol.name for rol in request.user.groups.all()],
            }
            return Response(userDict)
        return Response({'detail': "El usuario no se encuentra autenticado"}, status=status.HTTP_401_UNAUTHORIZED)



