from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .backends import CustomAuthBackend
from django.contrib import messages
from django.http import JsonResponse
from .models import Usuarios, Conductores, Vehiculos, Rutas, Viajes, Roles, Tickets, generar_nombre_usuario
from .forms import SignInForm, SignUpForm, NuevoUsuarioForm, NuevoAdminForm, NuevoClienteForm, NuevoConductorForm,  NuevoViajesForm, NuevoVehiculoForm, NuevaRutaForm


def signin(request):
    if request.method == "GET":
        form = SignInForm()
        return render(request, "signin.html", {"form": form})
    else:
        form = SignInForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            usuario = CustomAuthBackend.authenticate(
                nombre_usuario=usuario, contraseña=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('pagina_principal')
        return render(request, "signin.html", {"form": form})


def signup(request):
    if request.method == "GET":
        formUsuario = SignUpForm()
        formCliente = NuevoClienteForm()
        return render(request, "signup.html", {"formUsuario": formUsuario, "formCliente": formCliente})
    else:
        formUsuario = NuevoUsuarioForm(request.POST)
        formCliente = NuevoClienteForm(request.POST)

        if formUsuario.is_valid() and formCliente.is_valid():
            nombre = formCliente.cleaned_data['nombre']
            print(nombre)
            apellido = formCliente.cleaned_data['apellido']
            print(apellido)

            nombre_usuario = generar_nombre_usuario(nombre, apellido)
            print(nombre_usuario)

            usuario = formUsuario.save(commit=False, rol=2)
            cliente = formCliente.save(commit=False)

            usuario.nombreusuario = nombre_usuario
            usuario.save()
            cliente.save()

            login(request, usuario)
            return redirect('pagina_principal')

        messages.error(
            request, 'Ha ocurrido un error, por favor intente de nuevo.')
        return render(request, "signup.html", {"formUsuario": formUsuario, "formCliente": formCliente})


# @login_required
# def info_view(request):
#     objects = Usuarios.objects.all()

#     data = [{'Id': obj.usuarioid, 'Nombre': obj.nombreusuario}
#             for obj in objects]

#     return JsonResponse({'Respuestas': data})


@login_required
def pagina_principal(request):
    rol = "capas/baseadmin.html" if request.user.rolid.rolid == 1 else "capas/base.html"

    return render(request, "index.html", {
        'rol': rol,
        'usuario': request.user
    })


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


@login_required
def elegir_usuario(request):
    roles = Roles.objects.all()
    return render(request, "admin/elegir_usuario.html", {"roles": roles, "usuario": request.user})


@login_required
def create_usuario(request):
    rol = request.GET.get('inputRoles')
    if request.method == "GET":
        if rol == '1':
            form = NuevoAdminForm()
        elif rol == '2':
            formUsuario = NuevoUsuarioForm()
            formCliente = NuevoClienteForm()
        else:
            formUsuario = NuevoUsuarioForm()
            formConductor = NuevoConductorForm()

        return render(request, "admin/create_usuario.html", {
            "usuario": request.user,
            "rol": rol,
            "form": form if rol == '1' else None,
            "formUsuario": formUsuario if rol == '2' or rol == '3' else None,
            "formCliente": formCliente if rol == '2' else None,
            "formConductor": formConductor if rol != '1' and rol != '2' else None
        })

    else:
        if request.GET.get('rol') == '1':
            form = NuevoAdminForm(request.POST)
            if form.is_valid():
                form.save()

                messages.success(
                    request, 'Se ha registrado el usuario de manera exitosa.')
                return redirect('rol_usuario')

        if request.GET.get('rol') == '2':
            formUsuario = NuevoUsuarioForm(request.POST)
            formCliente = NuevoClienteForm(request.POST)

            if formUsuario.is_valid() and formCliente.is_valid():
                nombre = formCliente.cleaned_data['nombre']
                apellido = formCliente.cleaned_data['apellido']

                nombre_usuario = generar_nombre_usuario(nombre=nombre, apellido=apellido)

                cliente = formCliente.save(commit=False)
                usuario = formUsuario.save(commit=False, rol=2)

                usuario.nombreusuario = nombre_usuario
                cliente.save()
                usuario.save()

                messages.success(
                    request, 'Se ha registrado el usuario de manera exitosa.')
                return redirect('rol_usuario')

        else:
            formUsuario = NuevoUsuarioForm(request.POST)
            formConductor = NuevoConductorForm(request.POST)

            if formUsuario.is_valid() and formConductor.is_valid():
                nombre = formConductor.cleaned_data['nombre']
                apellido = formConductor.cleaned_data['apellido']

                nombre_usuario = generar_nombre_usuario(nombre, apellido)

                conductor = formConductor.save(commit=False)
                usuario = formUsuario.save(commit=False, rol=3)

                usuario.nombreusuario = nombre_usuario
                conductor.save()
                usuario.save()

                messages.success(
                    request, 'Se ha registrado el usuario de manera exitosa.')
                return redirect('rol_usuario')

        messages.success(
            request, 'Ha ocurrido un error, por favor intente de nuevo')
        return redirect('rol_usuario')


@login_required
def create_ruta(request):
    if request.method == "GET":
        form = NuevaRutaForm()
        return render(request, "admin/create_ruta.html", {'form': form, 'usuario': request.user})
    else:
        form = NuevaRutaForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request, 'Se ha registrado la ruta de manera exitosa.')
            return redirect('pagina_principal')

        messages.error(
            request, 'Ha ocurrido un error, por favor intente de nuevo.')
        return redirect('nueva_ruta')


@login_required
def create_vehiculo(request):
    if request.method == "GET":
        form = NuevoVehiculoForm()
        return render(request, "admin/create_vehiculo.html", {"form": form})
    else:
        formVehiculo = NuevoVehiculoForm(request.POST)
        if formVehiculo.is_valid():
            formVehiculo.save(commit=False)
            formVehiculo.save()

            messages.success(
                request, 'Se ha registrado el vehiculo de manera exitosa.')
            return redirect('nuevo_vehiculo')

        messages.error(
            request, 'Ha ocurrido un error, por favor intente de nuevo.')
        return redirect('nuevo_vehiculo')


@login_required
def create_viaje(request):
    if request.method == "GET":
        form = NuevoViajesForm()
        return render(request, "admin/create_viaje.html", {"form": form})
    else:
        formViaje = NuevoViajesForm(request.POST)
        if formViaje.is_valid():
            formViaje.save(commit=False)
            formViaje.save()

            messages.success(
                request, 'Se ha registrado el viaje de manera exitosa.')
            return redirect('nuevo_viaje')

        messages.error(
            request, 'Ha ocurrido un error, por favor intente de nuevo.')
        return redirect('nuevo_viaje')


@login_required
def see_rutas(request):
    if request.method == "GET":
        return render(request, "admin/view_rutas.html")
    else:
        formViaje = NuevoViajesForm(request.POST)
        if formViaje.is_valid():
            formViaje.save(commit=False)
            formViaje.save()

            messages.success(
                request, 'Se ha registrado el viaje de manera exitosa.')
            return redirect('nuevo_viaje')

        messages.error(
            request, 'Ha ocurrido un error, por favor intente de nuevo.')
        return redirect('nuevo_viaje')


@login_required
def see_rutas(request):
    if request.method == "GET":
        rutas = Rutas.objects.all()
        return render(request, "admin/view_rutas.html", {'rutas': rutas, 'usuario': request.user})


@login_required
def see_viajes(request):
    if request.method == "GET":
        viajes = Viajes.objects.all()
        return render(request, "admin/view_viajes.html", {'viajes': viajes, 'usuario': request.user})


@login_required
def see_vehiculos(request):
    if request.method == "GET":
        vehiculos = Vehiculos.objects.all()
        return render(request, "admin/view_vehiculos.html", {'vehiculos': vehiculos, 'usuario': request.user})


@login_required
def see_tickets(request):
    if request.method == "GET":
        tickets = Tickets.objects.all()
        return render(request, "admin/view_tickets.html", {"ticket": tickets, 'usuario': request.user})


@login_required
def see_usuarios(request):
    if request.method == "GET":
        usuarios = Usuarios.objects.all()
        return render(request, "admin/view_usuarios.html", {'usuarios': usuarios, 'usuario': request.user})


@login_required
def see_conductores(request):
    if request.method == "GET":
        conductores = Conductores.objects.all()
        return render(request, "admin/view_conductores.html", {'conductores': conductores, 'usuario': request.user})
