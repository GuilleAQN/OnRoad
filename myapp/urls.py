from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin,name="login"),
    path('about/', views.info_view,name="login"),
    #path("registro_cliente/",views.registro_cliente,name="registro"),
    path("create_conductor/",views.create_conductor,name="cr_conductores"),
    path("create_ruta/",views.create_ruta,name="cr_rutas"),
    path("create_viaje/",views.create_viaje,name="cr_viajes"),
    path("create_vehiculo/",views.create_vehiculo,name="cr_vehiculos"),
    #path("create_admin/",views.create_admin,name="cr_admins"),
    #path("view_conductor/",views.view_conductor,name="vw_conductores"),
    #path("view_ruta/",views.view_ruta,name="vw_rutas"),
    #path("view_tickets/",views.view_tickets,name="vw_tickets"),
    #path("view_usuarios/",views.view_usuarios,name="vw_usuarios"),
    #path("view_vehiculos/",views.view_vehiculos,name="vw_vehiculos"),
    #path("view_viajes/",views.view_viajes,name="vw_viajes"),
    #path("venta_ticket/",views.venta_ticket,name="venta"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
