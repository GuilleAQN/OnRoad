# Generated by Django 5.0.8 on 2024-12-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_usuarios_is_active_usuarios_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
