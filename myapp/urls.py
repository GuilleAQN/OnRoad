from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('signout/', views.signout, name="signout"),
    # path('prueba/', views.info_view),

    path("elegir_usuario/", views.elegir_usuario, name="rol_usuario"),
    path("elegir_usuario/registro_usuario/",
         views.create_usuario, name="nuevo_usuario"),
    path("registro_ruta/", views.create_ruta, name="nueva_ruta"),
    path("registro_viaje/", views.create_viaje, name="nuevo_viaje"),
    path("registro_vehiculo/", views.create_vehiculo, name="nuevo_vehiculo"),

    path("ver_rutas/", views.see_rutas, name="ver_rutas"),
    path("ver_viaje/", views.see_viajes, name="ver_viajes"),
    path("ver_vehiculos/", views.see_vehiculos, name="ver_vehiculos"),
    path("ver_tickets/", views.see_tickets, name="ver_tickets"),
    path("ver_usuarios/", views.see_usuarios, name="ver_usuarios"),
    path("ver_conductores/", views.see_conductores, name="ver_conductores")

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
