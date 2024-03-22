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
    return render (request,"admin/create_viajes.html")

def create_admin(request):
    return render (request,"admin/create_admin.html")

def view_conductor(request):
    return render (request,"admin/view_conductor.html")

def view_ruta(request):
    return render (request,"admin/view_ruta.html")

def view_tickets(request):
    return render (request,"admin/view_tickets.html")

def view_usuarios(request):
    return render (request,"admin/view_usuarios.html")

def view_vehiculos(request):
    return render (request,"admin/view_vehiculos.html") 

def view_viajes(request):
    return render (request,"admin/view_viajes.html")

def venta_ticket(request):
    return render (request,"capas/venta_ticket.html")   