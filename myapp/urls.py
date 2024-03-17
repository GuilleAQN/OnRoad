from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("registro_cliente/", views.registro_cliente),
    path("create_conductor/", views.create_conductor),
    path("create_ruta/", views.create_ruta),
    path("create_viaje/", views.create_viaje),
    path("create_vehiculo/", views.create_vehiculo),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
