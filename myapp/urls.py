from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('signout/', views.signout, name="signout"),
    path('prueba/', views.info_view),

    path("elegir_usuario/", views.elegir_usuario, name="rol_usuario"),
    path("elegir_usuario/registro_usuario/",
         views.create_usuario, name="nuevo_usuario"),
    path("registro_ruta/", views.create_ruta, name="nueva_ruta"),
    path("registro_viaje/", views.create_viaje, name="nuevo_viaje"),
    path("registro_vehiculo/", views.create_vehiculo, name="nuevo_vehiculo"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
