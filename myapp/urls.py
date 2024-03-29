from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="login"),

    path("elegir_usuario/", views.elegir_usuario, name="rol_usuario"),
    path("elegir_usuario/registro_usuario/", views.create_usuario, name="registro_usuario"),
    path("create_ruta/", views.create_ruta, name="registro_ruta"),
    path("create_viaje/", views.create_viaje, name="registro_viaje"),
    path("create_vehiculo/", views.create_vehiculo, name="registro_vehiculo"),

    path("ver_rutas/", views.see_rutas, name="ver_rutas"),
    path("ver_viajes/", views.see_viajes, name="ver_viajes"),
    path("ver_vehiculos/", views.see_vehiculos, name="ver_vehiculos"),
    path("ver_tickets/", views.see_tickets, name="ver_tickets"),
    path("ver_usuarios/", views.see_usuarios, name="ver_usuarios"),
    path("ver_conductores/", views.see_conductores, name="ver_conductores"),

    path("eliminar_ruta/<int:id>", views.delete_ruta, name="eliminar_ruta"),
    path("eliminar_viaje/<int:id>", views.delete_viaje, name="eliminar_viaje"),
    path("eliminar_vehiculo/<int:id>", views.delete_vehiculo, name="eliminar_vehiculo"),
    path("eliminar_usuario/<uuid:id>", views.delete_usuario, name="eliminar_usuario"),
    path("eliminar_conductor/<int:id>", views.delete_conductor, name="eliminar_conductor"),


    # path("venta_ticket/",views.venta_ticket,name="venta"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
