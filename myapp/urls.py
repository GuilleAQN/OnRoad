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
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
