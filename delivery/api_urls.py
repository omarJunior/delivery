from django.urls import path, include
from appPersona.viewsets import ApiCustomAuthToken

#Url de la apiRest
urlpatterns = [
    path("appConfiguracion/", include('appConfiguracion.routers')),
    path('appFactura/', include('appFactura.routers')),
    path('appPersona/', include('appPersona.routers')),
    path('auth-user/', ApiCustomAuthToken.as_view()),
]