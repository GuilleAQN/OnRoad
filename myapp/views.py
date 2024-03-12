from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios

def hello(request):
    return HttpResponse("<h1>Hola mundo</h1>")


def about(request):
    return HttpResponse("<h1>About</h1>")


def info_view(request):
    objects = Usuarios.objects.all()

    data = [{'Id': obj.usuarioid, 'Nombre': obj.nombreusuario}
            for obj in objects]

    return JsonResponse({'Respuestas': data})
