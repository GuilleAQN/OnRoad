from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from myapp import views 

# Create your views here.

def index(request):
    title = "OnRoad"
    return render(request, "index.html", {
        "title": title,
    })

def hello(request):
    return HttpResponse("<h1>Hola mundo</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def info_view(request):
    Usuarios = apps.get_model('myapp', 'Usuarios')
    objects = Usuarios.objects.all()

    data = [{'Id': obj.usuarioid, 'Nombre': obj.nombreusuario}
            for obj in objects]

    return JsonResponse({'Respuestas': data})

def registro_cliente(request):
    return render (request,"capas/clientes.html")

def create_conductor(request):
    return render (request,"admin/create_conductor.html")

def create_ruta(request):
    return render (request,"admin/create_ruta.html")

def create_vehiculo(request):
    return render (request,"admin/create_vehiculo.html")

def create_viaje(request):
    return render (request,"admin/create_viajes.html")

def create_admin(request):
    return render (request,"admin/create_admin.html")