# Generated by Django 5.0.2 on 2024-03-21 18:39

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('password', models.CharField(
                    max_length=128, verbose_name='password', )),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('usuarioid', models.UUIDField(default=uuid.uuid4,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreusuario', models.CharField(max_length=50,
                 unique=True, verbose_name='Nombre de usuario')),
                ('estado', models.CharField(blank=True,
                 max_length=10, null=True, verbose_name='Estado')),
                ('fechacreacion', models.DateTimeField(
                    auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('rolid', models.AutoField(primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('nombrerol', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('rutaid', models.AutoField(primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=100, verbose_name='Origen')),
                ('destino', models.CharField(max_length=100, verbose_name='Destino')),
                ('distancia', models.DecimalField(decimal_places=2,
                 max_digits=10, verbose_name='Distancia del viaje')),
                ('duracionestimada', models.DurationField(
                    verbose_name='Duración estimada')),
                ('preciobase', models.DecimalField(decimal_places=2,
                 max_digits=10, verbose_name='Precio base de la ruta')),
            ],
            options={
                'db_table': 'rutas',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('clienteid', models.AutoField(
                    primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(
                    max_length=50, verbose_name='Apellido')),
                ('correoelectronico', models.CharField(blank=True,
                 max_length=100, null=True, verbose_name='Correo Electrónico')),
                ('telefono', models.CharField(blank=True,
                 max_length=15, null=True, verbose_name='Teléfono')),
                ('direccion', models.CharField(blank=True,
                 max_length=100, null=True, verbose_name='Dirección')),
                ('usuarioid', models.OneToOneField(blank=True, db_column='usuarioid', null=True,
                 on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='ID de Usuario')),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Conductores',
            fields=[
                ('conductorid', models.AutoField(
                    primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(
                    max_length=50, verbose_name='Apellido')),
                ('licenciaconducir', models.CharField(
                    max_length=20, verbose_name='No. de Licencia')),
                ('telefono', models.CharField(blank=True,
                 max_length=15, null=True, verbose_name='Teléfono')),
                ('direccion', models.CharField(blank=True,
                 max_length=100, null=True, verbose_name='Dirección')),
                ('fechacontratacion', models.DateField(blank=True,
                 null=True, verbose_name='Fecha de Contratación')),
                ('usuarioid', models.OneToOneField(blank=True, db_column='usuarioid', null=True,
                 on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'conductores',
            },
        ),
        migrations.AddField(
            model_name='usuarios',
            name='rolid',
            field=models.ForeignKey(
                db_column='rolid', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.roles', verbose_name='ID del Rol'),
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('vehiculoid', models.AutoField(
                    primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('capacidad', models.IntegerField(
                    blank=True, null=True, verbose_name='Capacidad')),
                ('anofabricacion', models.IntegerField(
                    blank=True, null=True, verbose_name='Año de Fabriación')),
                ('placa', models.CharField(blank=True, max_length=20,
                 null=True, unique=True, verbose_name='No. de Placa')),
                ('estado', models.CharField(blank=True,
                 max_length=15, null=True, verbose_name='Estado')),
                ('conductorid', models.ForeignKey(blank=True, db_column='conductorid', null=True,
                 on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.conductores', verbose_name='ID del Conductor')),
            ],
            options={
                'db_table': 'vehiculos',
            },
        ),
        migrations.CreateModel(
            name='Viajes',
            fields=[
                ('viajeid', models.AutoField(primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('fechahorasalida', models.DateTimeField(
                    verbose_name='Hora de salida del viaje')),
                ('fechahorallegadaestimada', models.DateTimeField(
                    verbose_name='Hora estimada de llegada del viajes')),
                ('cuposdisponibles', models.IntegerField(
                    verbose_name='Tickets disponibles para viaje')),
                ('rutaid', models.ForeignKey(db_column='rutaid',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.rutas', verbose_name='ID de Ruta')),
                ('vehiculoid', models.ForeignKey(db_column='vehiculoid',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.vehiculos', verbose_name='ID de Vehiculo')),
            ],
            options={
                'db_table': 'viajes',
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticketid', models.AutoField(
                    primary_key=True, serialize=False, verbose_name='ID')),
                ('fechareservacion', models.DateTimeField(
                    blank=True, null=True, verbose_name='Fecha de Reservación')),
                ('estadoticket', models.CharField(blank=True,
                 max_length=10, null=True, verbose_name='Estado')),
                ('preciototal', models.DecimalField(decimal_places=2,
                 max_digits=10, verbose_name='Valor Total del Ticket')),
                ('clienteid', models.ForeignKey(db_column='clienteid',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.clientes', verbose_name='ID del Cliente')),
                ('viajeid', models.ForeignKey(db_column='viajeid',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.viajes', verbose_name='ID del Viaje')),
            ],
            options={
                'db_table': 'tickets',
            },
        ),
    ]
