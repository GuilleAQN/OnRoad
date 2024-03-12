from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.apps import apps


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
