# OnRoad

<div class="logo" align="center">
    <img src="https://onroad.sirv.com/Images/Logo-no-background.png" width="300" height="300" alt="Logo de la Compañia" style="margin-bottom: 5px;">
</div>

"OnRoad" es una aplicación web desarrollada con Django que ofrece funcionalidades relacionadas con pagos en línea a través de Stripe, un sistema intermediario de pagos online. La aplicación permite a los usuarios realizar pagos de forma segura utilizando la integración de Stripe, lo que proporciona una experiencia fluida y confiable para los clientes.

Además de las funcionalidades de pago, "OnRoad" puede incluir características adicionales relacionadas con la gestión de información de usuarios, como la creación de cuentas, la gestión de perfiles de usuario, entre otras.

## Configuración del Entorno

### Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Python (versión 3.11.8)

### Instalación

1. Crear un directorio para el repositorio:

```sh
mkdir Proyecto
cd Proyecto
```

2. Navega al directorio del proyecto:

```sh
cd OnRoad
```

3. Instalar el entorno virtual con el intérprete a usar:

```sh
pip install virtualenv -t "/ruta/del/intérprete"
```

4. Inicializar el entorno virtual:

```sh
.\.venv\Scripts\activate
```

5. Clonar el repositorio:

```sh
git clone https://github.com/GuilleAQN/OnRoad.git
```

6. Instala las dependencias principales:

```sh
pip install -r requirements.txt
```

En caso de querer desarrollar, instala las dependencias de desarrollo:

```sh
pip install -r requirements.dev.txt
```

Nota: Para esto, descargar [Stripe CLI](https://docs.stripe.com/stripe-cli), y usar la **STRIPE_SECRET_KEY** y la **STRIPE_PUBLIC_KEY** en un archivo ".env", y seguir la documentación de Stripe para correr este proyecto en local.

7. Aplica las migraciones de la base de datos:

```sh
python manage.py migrate
```

8. Ejecuta el servidor de desarrollo:

```sh
python manage.py runserver 3000
```

La aplicación estará disponible en `http://localhost:3000/`.

## Uso

## Stack Tecnológico

- **Django**: Framework web de Python.
- **Stripe**: Sistema intermediario de pagos online.
- **Bootstrap**: Framework CSS para desarrollo web responsivo.
- **PostgreSQL**: Sistema de gestión de bases de datos relacional.
- **Render**: Servicio de hosting para aplicaciones web.

[![Django](https://img.shields.io/badge/Django-5.0.2-brightgreen)](https://www.djangoproject.com/)
[![Stripe](https://img.shields.io/badge/Stripe-Payments-blue)](https://stripe.com/es)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-blueviolet)](https://getbootstrap.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://www.postgresql.org/)
[![Render](https://img.shields.io/badge/Render-Hosting-yellowgreen)](https://render.com/)

## Contribución

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/NuevoFeature`).
3. Haz commit de tus cambios (`git commit -m 'feat: Añadir un NuevoFeature'`).
4. Sube tus cambios (`git push origin feature/NuevoFeature`).
5. Abre un pull request.

## Contacto

Si tienes preguntas, comentarios o sugerencias sobre "OnRoad", no dudes en ponerte en contacto:

- **Nombre**: Omar Guillermo Aquino Mena (Back-End) y Angel Enrique de la Cruz Prevost (Front-End).
- **Correo Electrónico**: [omarguillermo1@gmail.com](mailto:omarguillermo1@gmail.com) y [ad21-1380@unphu.edu.do](mailto:ad21-1380@unphu.edu.do)

También puedes abrir un problema en el repositorio de GitHub si encuentras algún error o deseas solicitar una nueva característica.
