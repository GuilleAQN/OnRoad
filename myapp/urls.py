from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("elegir_usuario/", views.elegir_usuario, name="rol_usuario"),
    path("elegir_usuario/registro_usuario/", views.create_usuario, name="registro_usuario"),
    path("create_ruta/", views.create_ruta, name="registro_rutas"),
    path("create_viaje/", views.create_viaje, name="registro_viajes"),
    path("create_vehiculo/", views.create_vehiculo, name="registro_vehiculos"),

    path("ver_rutas/", views.see_rutas, name="ver_rutas"),
    path("ver_viajes/", views.see_viajes, name="ver_viajes"),
    path("ver_vehiculos/", views.see_vehiculos, name="ver_vehiculos"),
    path("ver_tickets/", views.see_tickets, name="ver_tickets"),
    path("ver_usuarios/", views.see_usuarios, name="ver_usuarios"),
    path("ver_conductores/", views.see_conductores, name="ver_conductores"),

    # path("venta_ticket/",views.venta_ticket,name="venta"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
