from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from myapp import views


def index(request):
    titulo = "OnRoad"
    return render(request, "index.html", {
        "titulo": titulo,
    })


def info_view(request):
    Usuarios = apps.get_model('myapp', 'Usuarios')
    objects = Usuarios.objects.all()

    data = [{'Id': obj.usuarioid, 'Nombre': obj.nombreusuario}
            for obj in objects]

    return JsonResponse({'Respuestas': data})


def registro_cliente(request):
    titulo = "Registro"
    return render(request, "capas/clientes.html", {'titulo': titulo})


def create_conductor(request):
    titulo = "Registro de Conductor"
    return render(request, "admin/create_conductor.html", {'titulo': titulo})


def create_ruta(request):
    titulo = "Registro de Ruta"
    return render(request, "admin/create_ruta.html", {'titulo': titulo})


def create_vehiculo(request):
    titulo = "Registro de Vehiculo"
    return render(request, "admin/create_vehiculo.html", {'titulo': titulo})


def create_viaje(request):
    titulo = "Registro de Viaje"
    return render(request, "admin/create_viajes.html", {'titulo': titulo})
