import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .backends import CustomAuthBackend
from django.contrib import messages
from django.http import JsonResponse
from .models import Usuarios, Clientes, Conductores, Vehiculos, Rutas, Viajes, Roles, Tickets, generar_nombre_usuario
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
        messages.error(
            request, 'Las credenciales no son correctas, por favor intente de nuevo.')
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
            apellido = formCliente.cleaned_data['apellido']

            nombre_usuario = generar_nombre_usuario(nombre, apellido)

            usuario = formUsuario.save(commit=False, rol=2)
            cliente = formCliente.save(commit=False, usuario=usuario)

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
def see_perfil(request):
    rol = "capas/baseadmin.html" if request.user.rolid.rolid == 1 else "capas/base.html"
    return render(request, "perfil.html", {"rol": rol, "usuario": request.user})


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

                nombre_usuario = generar_nombre_usuario(
                    nombre=nombre, apellido=apellido)

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

                usuario = formUsuario.save(commit=False, rol=3)
                conductor = formConductor.save(commit=False, usuario=usuario)

                usuario.nombreusuario = nombre_usuario
                usuario.save()
                conductor.save()

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
        return render(request, "admin/create_vehiculo.html", {"form": form, 'usuario': request.user})
    else:
        formVehiculo = NuevoVehiculoForm(request.POST)
        if formVehiculo.is_valid():
            formVehiculo.save(commit=False)
            formVehiculo.save()

            messages.success(
                request, 'Se ha registrado el vehiculo de manera exitosa.')
            return redirect('registro_vehiculo')

        messages.error(
            request, 'Ha ocurrido un error, por favor intente de nuevo.')
        return redirect('registro_vehiculo')


@login_required
def create_viaje(request):
    if request.method == "GET":
        form = NuevoViajesForm()
        return render(request, "admin/create_viaje.html", {"form": form, 'usuario': request.user})
    else:
        formViaje = NuevoViajesForm(request.POST)
        if formViaje.is_valid():
            formViaje.save(commit=False)
            formViaje.save()

            messages.success(
                request, 'Se ha registrado el viaje de manera exitosa.')
            return redirect('registro_viaje')

        messages.error(
            request, 'Ha ocurrido un error, por favor intente de nuevo.')
        return redirect('registro_viaje')


@login_required
def create_ruta(request):
    if request.method == "GET":
        form = NuevaRutaForm()
        return render(request, "admin/create_ruta.html", {"form": form, 'usuario': request.user})
    else:
        formRuta = NuevaRutaForm(request.POST)
        if formRuta.is_valid():
            formRuta.save(commit=False)
            formRuta.save()

            messages.success(
                request, 'Se ha registrado el viaje de manera exitosa.')
            return redirect('registro_viaje')

        messages.error(
            request, 'Ha ocurrido un error, por favor intente de nuevo.')
        return redirect('registro_viaje')


@login_required
def see_rutas(request):
    rutas = Rutas.objects.all()
    return render(request, "admin/view_rutas.html", {'rutas': rutas, 'usuario': request.user})


@login_required
def see_viajes(request):
    viajes = Viajes.objects.all()
    return render(request, "admin/view_viajes.html", {'viajes': viajes, 'usuario': request.user})


@login_required
def see_vehiculos(request):
    vehiculos = Vehiculos.objects.exclude(modelo='Placeholder')
    return render(request, "admin/view_vehiculos.html", {'vehiculos': vehiculos, 'usuario': request.user})


@login_required
def see_tickets(request):
    tickets = Tickets.objects.all()
    return render(request, "admin/view_tickets.html", {"ticket": tickets, 'usuario': request.user})


@login_required
def see_my_tickets(request):
    cliente = Clientes.objects.get(usuarioid=request.user.usuarioid)
    tickets = Tickets.objects.filter(clienteid=cliente.clienteid)
    return render(request, "my_tickets.html", {"ticket": tickets, 'usuario': request.user})


@login_required
def see_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, "admin/view_usuarios.html", {'usuarios': usuarios, 'usuario': request.user})


@login_required
def see_conductores(request):
    conductores = Conductores.objects.all()
    return render(request, "admin/view_conductores.html", {'conductores': conductores, 'usuario': request.user})


@login_required
def delete_ruta(request, id):
    ruta = get_object_or_404(Rutas, rutaid=id)
    ruta.delete()
    messages.success(request, 'Se ha eliminado la ruta de manera exitosa.')
    return redirect('ver_rutas')


@login_required
def delete_viaje(request, id):
    viaje = get_object_or_404(Viajes, viajeid=id)
    viaje.delete()
    messages.success(request, 'Se ha eliminado el viaje de manera exitosa.')
    return redirect('ver_viajes')


def delete_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculos, vehiculoid=id)
    vehiculo.delete()
    messages.success(request, 'Se ha eliminado el vehículo de manera exitosa.')
    return redirect('ver_vehiculos')


@login_required
def delete_usuario(request, id):
    usuario = get_object_or_404(Usuarios, usuarioid=id)
    usuario.delete()
    messages.success(request, 'Se ha eliminado el usuario de manera exitosa.')
    return redirect('ver_usuarios')


@login_required
def delete_conductor(request, id):
    conductor = get_object_or_404(Conductores, conductorid=id)
    conductor.delete()
    messages.success(
        request, 'Se ha eliminado el conductor de manera exitosa.')
    return redirect('ver_conductores')
