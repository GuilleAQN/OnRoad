# OnRoad

Descripción breve del proyecto.

## Configuración del Entorno

### Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Python (versión 3.11.8)

### Instalación

1. Clona el repositorio:

```sh
git clone https://github.com/GuilleAQN/OnRoad.git
```

2. Navega al directorio del proyecto:

```sh
cd OnRoad
```

3. Instala las dependencias principales:

```sh
pip install -r requirements.txt
```

En caso de querer desarrollar, instala las dependencias de desarrollo:

```sh
pip install -r requirements.dev.txt
```

4. Aplica las migraciones de la base de datos:

```sh
python manage.py migrate
```

5. Ejecuta el servidor de desarrollo:

```sh
python manage.py runserver 8000
```

La aplicación estará disponible en `http://localhost:8000/`.

## Uso

## Stack Tecnológico

- **Django**: Framework web de Python.
- **Bootstrap**: Framework CSS para desarrollo web responsivo.
- **PostgreSQL**: Sistema de gestión de bases de datos relacional.
- **Render**: Servicio de hosting para aplicaciones web.

[![Django](https://img.shields.io/badge/Django-5.0.2-brightgreen)](https://www.djangoproject.com/)
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
