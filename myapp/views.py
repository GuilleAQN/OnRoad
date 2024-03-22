from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .backends import CustomAuthBackend
from django.contrib import messages
from django.http import JsonResponse
from .models import Usuarios, Clientes, Roles, Conductores, Rutas, Vehiculos, Viajes, generar_nombre_usuario


def signin(request):
    if request.method == "GET":
        titulo = "OnRoad"
        return render(request, "signin.html", {"titulo": titulo})
    else:
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        usuario = CustomAuthBackend.authenticate(
            nombre_usuario=username, contraseña=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('pagina_principal')

        else:
            messages.error(request, 'El usuario o contraseña no existen.')
            return redirect('signin')


def signup(request):
    if request.method == "GET":
        titulo = "Nuevo Usuario"
        return render(request, "signup.html", {"titulo": titulo})
    else:
        if request.POST['inputPassword'] == request.POST['inputPasswordConfirm']:
            try:
                contraseña_hasheada = make_password(
                    request.POST['inputPassword'])
                nombre_usuario = generar_nombre_usuario(
                    request.POST['inputName'], request.POST['inputLastName'])

                rol = Roles.objects.get(pk=2)

                usuario = Usuarios(
                    nombreusuario=nombre_usuario,
                    password=contraseña_hasheada,
                    rolid=rol
                )
                usuario.save()

                cliente = Clientes.objects.create(
                    nombre=request.POST['inputName'],
                    apellido=request.POST['inputLastName'],
                    correoelectronico=request.POST['inputEmail'],
                    telefono=request.POST['inputPhone'],
                    direccion=request.POST['inputCity'],
                    usuarioid=usuario
                )
                cliente.save()

                return redirect('pagina_principal')

            except IntegrityError:
                messages.error(
                    request, 'Este correo ya ha sido utilizado, favor usar un correo diferente por cuenta.')
            return redirect('signup')
        else:
            messages.error(
                request, 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.')
            return redirect('signup')


@login_required(login_url='/')
def info_view(request):
    objects = Usuarios.objects.all()

    data = [{'Id': obj.usuarioid, 'Nombre': obj.nombreusuario}
            for obj in objects]

    return JsonResponse({'Respuestas': data})


@login_required(login_url='/')
def pagina_principal(request):
    titulo = "OnRoad"
    rol = "capas/baseadmin.html" if request.user.rolid.rolid == 1 else "capas/baseusuario.html"

    return render(request, "index.html", {
        'titulo': titulo,
        'rol': rol
    })


@login_required(login_url='/')
def signout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='/')
def elegir_usuario(request):
    roles = Roles.objects.all()
    return render(request, "admin/elegir_usuario.html", {"roles": roles})


@login_required(login_url='/')
def create_usuario(request):
    if request.method == "GET":
        titulo = "Nuevo Usuario"
        print(request.GET.get('inputRoles'))
        return render(request, "admin/create_usuario.html", {"titulo": titulo, "rol": request.GET.get('inputRoles')})
    else:
        if request.GET.get('inputRoles') == '1':
            try:
                contraseña_hasheada = make_password(
                    request.POST['pwd'])

                rol = Roles.objects.get(pk=1)

                usuario = Usuarios(
                    nombreusuario=request.POST['username'],
                    password=contraseña_hasheada,
                    rolid=rol
                )
                usuario.save()

            except IntegrityError:
                messages.error(
                    request, 'Ha ocurrido un error, por favor intente de nuevo.')
                return render(request, "admin/create_usuario.html", {"rol": 1})

        elif request.GET.get('inputRoles') == 2:
            try:
                contraseña_hasheada = make_password(
                    request.POST['inputPassword'])
                nombre_usuario = generar_nombre_usuario(
                    request.POST['inputName'], request.POST['inputLastName'])

                rol = Roles.objects.get(pk=2)

                usuario = Usuarios(
                    nombreusuario=nombre_usuario,
                    password=contraseña_hasheada,
                    rolid=rol
                )
                usuario.save()

                cliente = Clientes.objects.create(
                    nombre=request.POST['inputName'],
                    apellido=request.POST['inputLastName'],
                    correoelectronico=request.POST['inputEmail'],
                    telefono=request.POST['inputPhone'],
                    direccion=request.POST['inputCity'],
                    usuarioid=usuario
                )
                cliente.save()

                return redirect('pagina_principal')

            except IntegrityError:
                messages.error(
                    request, 'Ha ocurrido un error, por favor intente de nuevo.\n Recomendación: Use un correo distinto')
                return render(request, "admin/create_usuario.html", {"rol": 2})

        elif request.GET.get('inputRoles') == 3:
            try:
                contraseña_hasheada = make_password(
                    request.POST['inputPassword'])
                nombre_usuario = generar_nombre_usuario(
                    request.POST['inputName'], request.POST['inputLastName'])

                rol = Roles.objects.get(pk=request.GET.get('inputRoles'))

                usuario = Usuarios(
                    nombreusuario=nombre_usuario,
                    contraseñahash=contraseña_hasheada,
                    rolid=rol
                )
                usuario.save()

                conductor = Conductores.objects.create(
                    nombre=request.POST['inputName'],
                    apellido=request.POST['inputLastName'],
                    telefono=request.POST['inputPhone'],
                    direccion=request.POST['inputCity'],
                    licenciaconducir=request.POST['inputLicense'],
                    fechacontratacion=request.POST['inputDateContract'],
                    usuarioid=usuario
                )
                conductor.save()

            except IntegrityError:
                messages.error(
                    request, 'Ha ocurrido un error, por favor intente de nuevo.')
                return render(request, "admin/create_usuario.html", {"rol": 3})

        messages.success(
            request, 'Se ha registrado el usuario de manera exitosa.')
        return redirect('pagina_principal')


@login_required(login_url='/')
def create_conductor(request):
    if request.method == "GET":
        titulo = "Nuevo Conductor"
        return render(request, "admin/create_conductor.html", {"titulo": titulo})
    else:
        contraseña_hasheada = make_password(
            request.POST['inputPassword'])
        nombre_usuario = generar_nombre_usuario(
            request.POST['inputName'], request.POST['inputLastName'])

        rol = Roles.objects.get(pk=3)

        usuario = Usuarios(
            nombreusuario=nombre_usuario,
            contraseñahash=contraseña_hasheada,
            rolid=rol
        )
        usuario.save()

        conductor = Conductores.objects.create(
            nombre=request.POST['inputName'],
            apellido=request.POST['inputLastName'],
            telefono=request.POST['inputPhone'],
            direccion=request.POST['inputCity'],
            licenciaconducir=request.POST['inputLicense'],
            fechacontratacion=request.POST['inputDateContract'],
            usuarioid=usuario
        )
        conductor.save()

        return redirect('signin')


@login_required(login_url='/')
def create_ruta(request):
    if request.method == "GET":
        titulo = "Nueva Ruta"
        return render(request, "admin/create_ruta.html", {"titulo": titulo})
    else:
        try:
            ruta = Rutas.objects.create(
                origen=request.POST['inputOrigin'],
                destino=request.POST['inputDestiny'],
                distancia=request.POST['inputDistance'],
                duracionestimada=request.POST['inputDuration'],
                preciobase=request.POST['inputPrice'],
            )
            ruta.save()

            messages.success(
                request, 'Se ha registrado la ruta de manera exitosa.')
            return redirect('pagina_principal')

        except IntegrityError:
            messages.error(
                request, 'Ha ocurrido un error, por favor intente de nuevo.')
            return redirect('nueva_ruta')


@login_required(login_url='/')
def create_vehiculo(request):
    if request.method == "GET":
        titulo = "Nuevo Vehiculo"
        conductores = Conductores.objects.all()
        return render(request, "admin/create_vehiculo.html", {"titulo": titulo, "conductores": conductores})
    else:
        try:
            conductor = Conductores.objects.get(pk=request.POST['inputDriver'])

            vehiculo = Vehiculos.objects.create(
                marca=request.POST['inputBrand'],
                modelo=request.POST['inputModel'],
                capacidad=request.POST['inputCapacity'],
                anofabricacion=request.POST['inputFabrication'],
                placa=request.POST['inputPlate'],
                estado=request.POST['inputState'],
                conductorid=conductor
            )
            vehiculo.save()

            messages.success(
                request, 'Se ha registrado el vehiculo de manera exitosa.')
            return redirect('pagina_principal')

        except IntegrityError:
            messages.error(
                request, 'Ha ocurrido un error, por favor intente de nuevo.')
            return redirect('nuevo_vehiculo')


@login_required(login_url='/')
def create_viaje(request):
    if request.method == "GET":
        vehiculos = Vehiculos.objects.all()
        rutas = Rutas.objects.all()
        titulo = "Nuevo Viaje"
        return render(request, "admin/create_viaje.html", {"titulo": titulo, "vehiculos": vehiculos, "rutas": rutas})
    else:
        try:
            ruta = Rutas.objects.get(pk=request.POST['inputRoutes'])
            vehiculo = Vehiculos.objects.get(
                pk=request.POST['inputVehiculesRoutes'])

            viaje = Viajes.objects.create(
                rutaid=ruta,
                vehiculoid=vehiculo,
                fechahorasalida=request.POST['inputDateDeparture'],
                fechahorallegadaestimada=request.POST['inputDateArrive'],
                cuposdisponibles=request.POST['inputQuotas'],
            )
            viaje.save()

            messages.success(
                request, 'Se ha registrado el viaje de manera exitosa.')
            return redirect('pagina_principal')

        except IntegrityError:
            messages.error(
                request, 'Ha ocurrido un error, por favor intente de nuevo.')
            return redirect('nuevo_viaje')
