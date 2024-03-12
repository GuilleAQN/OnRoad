from django.db import models


class Clientes(models.Model):
    clienteid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correoelectronico = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.OneToOneField(
        'Usuarios', models.DO_NOTHING, db_column='usuarioid', blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        db_table = 'clientes'


class Conductores(models.Model):
    conductorid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fechacontratacion = models.DateField(blank=True, null=True)
    usuarioid = models.OneToOneField(
        'Usuarios', models.DO_NOTHING, db_column='usuarioid', blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        db_table = 'conductores'


class Roles(models.Model):
    rolid = models.AutoField(primary_key=True)
    nombrerol = models.CharField(max_length=50)

    class Meta:
        app_label = 'myapp'
        db_table = 'roles'


class Rutas(models.Model):
    rutaid = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    duracionestimada = models.DurationField()
    preciobase = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'myapp'
        db_table = 'rutas'


class Tickets(models.Model):
    ticketid = models.AutoField(primary_key=True)
    clienteid = models.ForeignKey(
        Clientes, models.DO_NOTHING, db_column='clienteid')
    viajeid = models.ForeignKey(
        'Viajes', models.DO_NOTHING, db_column='viajeid')
    fechareservacion = models.DateTimeField(blank=True, null=True)
    estadoticket = models.CharField(max_length=10, blank=True, null=True)
    preciototal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'myapp'
        db_table = 'tickets'


class Usuarios(models.Model):
    usuarioid = models.UUIDField(primary_key=True)
    nombreusuario = models.CharField(max_length=50)
    contraseñahash = models.CharField(max_length=128)
    estado = models.CharField(max_length=10, blank=True, null=True)
    rolid = models.ForeignKey(Roles, models.DO_NOTHING, db_column='rolid')
    fechacreacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        db_table = 'usuarios'


class Vehiculos(models.Model):
    vehiculoid = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    capacidad = models.IntegerField(blank=True, null=True)
    anofabricacion = models.IntegerField(blank=True, null=True)
    placa = models.CharField(unique=True, max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    conductorid = models.ForeignKey(
        Conductores, models.DO_NOTHING, db_column='conductorid', blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        db_table = 'vehiculos'


class Viajes(models.Model):
    viajeid = models.AutoField(primary_key=True)
    rutaid = models.ForeignKey(Rutas, models.DO_NOTHING, db_column='rutaid')
    vehiculoid = models.ForeignKey(
        Vehiculos, models.DO_NOTHING, db_column='vehiculoid')
    fechahorasalida = models.DateTimeField()
    fechahorallegadaestimada = models.DateTimeField()
    cuposdisponibles = models.IntegerField()

    class Meta:
        app_label = 'myapp'
        db_table = 'viajes'
