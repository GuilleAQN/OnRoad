"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from email.policy import default
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
SECRET_KEY = os.environ.get(
    'SECRET_KEY', default='-+8$u$dwr4=mua7w91w__foul0z%*j*4_2y07e3!ak(qrk#i6nogdsfd')

DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Application definition
INSTALLED_APPS = [
    'myapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASE_DEV_URL = os.getenv('DATABASE_DEV_URL')
DATABASE_PROD_URL = os.getenv('DATABASE_PROD_URL')

DATABASES = {}

if DATABASE_DEV_URL:
    DATABASES.update(development={
        'ENGINE': 'django.db.backends.postgresql', **dj_database_url.parse(DATABASE_DEV_URL)})

if DATABASE_PROD_URL:
    DATABASES.update(production={
        'ENGINE': 'django.db.backends.postgresql', **dj_database_url.parse(DATABASE_PROD_URL)})

ENVIRONMENT = os.getenv('DJANGO_ENV', 'production')
DATABASE_CONFIG = DATABASES.get(ENVIRONMENT, DATABASES['production'])

DATABASES['default'] = DATABASE_CONFIG


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SESSION_EXPIRE_SECONDS = 5400
SESSION_TIMEOUT_REDIRECT = '/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

AUTH_USER_MODEL = 'myapp.Usuarios'


# Internationalization
LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Directorios adicionales donde se buscarán archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myapp/static'),
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
