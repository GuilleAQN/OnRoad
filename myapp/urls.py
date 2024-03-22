from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.info_view),
    path("registro_cliente/",views.registro_cliente),
    path("create_conductor/",views.create_conductor),
    path("create_ruta/",views.create_ruta),
    path("create_viaje/",views.create_viaje),
    path("create_vehiculo/",views.create_vehiculo),
    path("create_admin/",views.create_admin),
    path("view_conductor/",views.view_conductor),
    path("view_ruta/",views.view_ruta),
    path("view_tickets/",views.view_tickets),
    path("view_usuarios/",views.view_usuarios),
    path("view_vehiculos/",views.view_vehiculos),
    path("view_viajes/",views.view_viajes),
    path("venta_ticket/",views.venta_ticket),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
