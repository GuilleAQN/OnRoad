from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

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
    objects = Usuarios.objects.all()

    data = [{'Id': obj.usuarioid, 'Nombre': obj.nombreusuario}
            for obj in objects]

    return JsonResponse({'Respuestas': data})
