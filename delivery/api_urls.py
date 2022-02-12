from django.urls import path, include
from appConfiguracion.urls import router as appRutesConfiguracion
from appFactura.urls import router as appRoutesFactura
from appPersona.urls import router as appRoutesPersona


from appPersona.viewsets import ApiCustomAuthToken

#Url de la apiRest
urlpatterns = [
    path("appConfiguracion/", include(appRutesConfiguracion.urls)),
    path('appFactura/', include(appRoutesFactura.urls)),
    path('appPersona/', include(appRoutesPersona.urls)),
    path('auth-user/', ApiCustomAuthToken.as_view()),
]