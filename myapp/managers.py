from django.contrib.auth.base_user import BaseUserManager


class CustomUsuarioManager(BaseUserManager):
    def create_user(self, nombreusuario, contraseña, rolid, **extra_fields):
        if not nombreusuario:
            raise ValueError('El nombre de usuario debe ser definido.')

        user = self.model(
            nombreusuario=nombreusuario,
            rolid=rolid,
            ** extra_fields
        )
        user.set_contraseña(contraseña)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombreusuario, contraseña, rolid, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(nombreusuario, contraseña, rolid, **extra_fields)
