# Generated by Django 5.0.2 on 2024-03-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_usuarios_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculos',
            name='estado',
            field=models.CharField(blank=True, choices=[('Disponible', 'DISPONIBLE'), ('Ocupado', 'OCUPADO'), ('Mantenimiento', 'MANTENIMIENTO')], default='Disponible', max_length=15, null=True, verbose_name='Estado'),
        ),
    ]
