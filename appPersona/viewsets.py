from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import viewsets, status, exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

from appConfiguracion.models import TipoIndetificacion

from .models import Cliente, Persona
from .serializers import ClienteSerializer, PersonaSerializer, UserSerializers

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer

    #Creacion de un cliente
    @action(detail=False, methods=['post'], url_path="registro-cliente", url_name="registro_cliente")
    def registro_cliente(self, request):
        id_user = request.data['id_user']
        codigo = request.data['codigo']
        tipoIdentificacion = request.data['tipoIndentificacion']
        numeroIdentificacion = request.data['numeroIdentificacion']
        nombres = request.data['nombres']
        apellidos = request.data['apellidos']
        correo_electronico = request.data['correo_electronico']
        fecha_nacimiento = request.data['fecha_nacimiento']
        edad = request.data['edad']
        direccion = request.data['direccion']
        telefono = request.data['telefono']
        descuento = request.data['descuento']
        
        obj_cliente = Cliente()
        obj_cliente.codigo = codigo
        obj_cliente.tipoIdentificacion = tipoIdentificacion
        obj_cliente.numeroIdentificacion = numeroIdentificacion
        obj_cliente.nombres = nombres
        obj_cliente.apellidos = apellidos
        obj_cliente.correo_electronico = correo_electronico
        obj_cliente.fecha_nacimiento = fecha_nacimiento
        obj_cliente.edad = edad
        obj_cliente.direccion = direccion
        obj_cliente.telefono = telefono
        obj_cliente.descuento = descuento
        obj_cliente.obj_user_referenciado = User()
        obj_cliente.obj_user_referenciado.id = id_user
        obj_cliente.save()
        

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all().order_by('id')
    serializer_class = PersonaSerializer
    
    @action(detail=False, methods=['get'], url_path="get_grupos", url_name="get-grupos", permission_classes = (AllowAny, ))
    def get_grupos(self, request):
        grupos = Group.objects.all().values()
        return Response(grupos)

    #Creacion para usuarios con roles
    @action(detail=False, methods=['post'], url_path="register_persona", url_name="register-persona" , permission_classes = (AllowAny, ))
    def registro(self, request):
        username = request.data['username']
        tipoIdentificacion = request.data['tipoIdentificacion']
        numeroIdentificacion = request.data['numeroIdentificacion']
        nombres = request.data['nombres']
        apellidos = request.data['apellidos']
        correo_electronico = request.data['correo_electronico']
        edad = request.data['edad']
        direccion = request.data['direccion']
        telefono = request.data['telefono'] 
        password = request.data['password']
        rol_persona = request.data['rol_persona']

        user_existe = User.objects.filter(username = username)
        email_existe = User.objects.filter(email = correo_electronico)
        if user_existe.count() > 0 or email_existe.count() > 0:
            return Response({'error': 'Ya se encuentra registrado ese username o email'})
        user = User()
        user.username = username
        user.first_name = nombres
        user.last_name = apellidos
        user.email = correo_electronico
        user.password = make_password(password)
        user.save()
        try:
            grupo_obj = Group.objects.get(id = rol_persona)
        except:
            grupo_obj = None
        
        if grupo_obj is not None:
            user.groups.add(grupo_obj)
        user.save()

        persona = Persona()
        persona.obj_user = user
        persona.tipoIdentificacion = TipoIndetificacion()
        persona.tipoIdentificacion.id = tipoIdentificacion
        persona.numeroIdentificacion = numeroIdentificacion
        persona.nombres = nombres
        persona.apellidos = apellidos
        persona.correo_electronico = correo_electronico
        persona.edad = edad
        persona.direccion = direccion
        persona.telefono = telefono
        persona.save()
        try:
            grupo_rol = Group.objects.filter(id = rol_persona)
        except:
            grupo_rol = None
        if grupo_rol is not None:
            #Instancias de QuerySet[]
            persona.rol_persona.set(grupo_rol)
        persona.save()
        return Response({'msg': 'Datos guardados correctamente'})
        

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
                    "username": user.username,
                    "correo_electronico": user.email,
                    "fullname": user.get_full_name(),
                    "tipo_identificacion": tipo_identificacion,
                    "nro_identificacion": nro_indentificacion,
                    "roles": [rol.name for rol in user.groups.all()],
                    "refresh": str(refresh),
                    "access_token": str(refresh.access_token)
                }
                return Response({'datos': userDict}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'El usuario no se encuentra activo'})
                #raise exceptions.AuthenticationFailed("El usuario no se encuentra activo")
        else:
            return Response({'error': 'Verifique su usuario y contraseña'})
            #raise exceptions.AuthenticationFailed("Verifique su usuario y contraseña")

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-is_active')
    serializer_class = UserSerializers

    def get_queryset(self):
        qs = User.objects.all().order_by('-is_active')
        id = self.request.query_params.get('id_user')
        if id is not None:
            qs = qs.filter(user_persona__obj_user = id)
            return qs
        else:
            return qs


