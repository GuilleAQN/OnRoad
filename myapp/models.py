from tabnanny import verbose
from django.db import models


class Clientes(models.Model):
    clienteid = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    correoelectronico = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Correo Electrónico')
    telefono = models.CharField(
        max_length=15, blank=True, null=True, verbose_name='Teléfono')
    direccion = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Dirección')
    usuarioid = models.OneToOneField(
        'Usuarios', models.DO_NOTHING, db_column='usuarioid', blank=True, null=True, verbose_name='ID de Usuario')

    class Meta:
        app_label = 'myapp'
        db_table = 'clientes'


class Conductores(models.Model):
    conductorid = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    licenciaconducir = models.CharField(
        max_length=20, verbose_name='No. de Licencia')
    telefono = models.CharField(
        max_length=15, blank=True, null=True, verbose_name='Teléfono')
    direccion = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Dirección')
    fechacontratacion = models.DateField(
        blank=True, null=True, verbose_name='Fecha de Contratación')
    usuarioid = models.OneToOneField(
        'Usuarios', models.DO_NOTHING, db_column='usuarioid', blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        db_table = 'conductores'


class Roles(models.Model):
    rolid = models.AutoField(primary_key=True, verbose_name='ID')
    nombrerol = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        app_label = 'myapp'
        db_table = 'roles'


class Rutas(models.Model):
    rutaid = models.AutoField(primary_key=True, verbose_name='ID')
    origen = models.CharField(max_length=100, verbose_name='Origen')
    destino = models.CharField(max_length=100, verbose_name='Destino')
    distancia = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Distancia del viaje')
    duracionestimada = models.DurationField(verbose_name='Duración estimada')
    preciobase = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Precio base de la ruta')

    class Meta:
        app_label = 'myapp'
        db_table = 'rutas'


class Tickets(models.Model):
    ticketid = models.AutoField(primary_key=True, verbose_name='ID')
    clienteid = models.ForeignKey(
        Clientes, models.DO_NOTHING, db_column='clienteid', verbose_name='ID del Cliente')
    viajeid = models.ForeignKey(
        'Viajes', models.DO_NOTHING, db_column='viajeid', verbose_name='ID del Viaje')
    fechareservacion = models.DateTimeField(
        blank=True, null=True, verbose_name='Fecha de Reservación')
    estadoticket = models.CharField(
        max_length=10, blank=True, null=True, verbose_name='Estado')
    preciototal = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Valor Total del Ticket')

    class Meta:
        app_label = 'myapp'
        db_table = 'tickets'


class Usuarios(models.Model):
    usuarioid = models.UUIDField(primary_key=True, verbose_name='ID')
    nombreusuario = models.CharField(max_length=50, verbose_name='Nombre')
    contraseñahash = models.CharField(
        max_length=128, verbose_name='Contraseña')
    estado = models.CharField(
        max_length=10, blank=True, null=True, verbose_name='Estado')
    rolid = models.ForeignKey(Roles, models.DO_NOTHING,
                              db_column='rolid', verbose_name='ID del Rol')
    fechacreacion = models.DateTimeField(
        blank=True, null=True, verbose_name='Fecha de creación')

    class Meta:
        app_label = 'myapp'
        db_table = 'usuarios'


class Vehiculos(models.Model):
    vehiculoid = models.AutoField(primary_key=True, verbose_name='ID')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    capacidad = models.IntegerField(
        blank=True, null=True, verbose_name='Capacidad')
    anofabricacion = models.IntegerField(
        blank=True, null=True, verbose_name='Año de Fabriación')
    placa = models.CharField(unique=True, max_length=20,
                             blank=True, null=True, verbose_name='No. de Placa')
    estado = models.CharField(
        max_length=15, blank=True, null=True, verbose_name='Estado')
    conductorid = models.ForeignKey(
        Conductores, models.DO_NOTHING, db_column='conductorid', blank=True, null=True, verbose_name='ID del Conductor')

    class Meta:
        app_label = 'myapp'
        db_table = 'vehiculos'


class Viajes(models.Model):
    viajeid = models.AutoField(primary_key=True, verbose_name='ID')
    rutaid = models.ForeignKey(
        Rutas, models.DO_NOTHING, db_column='rutaid', verbose_name='ID de Ruta')
    vehiculoid = models.ForeignKey(
        Vehiculos, models.DO_NOTHING, db_column='vehiculoid', verbose_name='ID de Vehiculo')
    fechahorasalida = models.DateTimeField(
        verbose_name='Hora de salida del viaje')
    fechahorallegadaestimada = models.DateTimeField(
        verbose_name='Hora estimada de llegada del viajes')
    cuposdisponibles = models.IntegerField(
        verbose_name='Tickets disponibles para viaje')

    class Meta:
        app_label = 'myapp'
        db_table = 'viajes'
