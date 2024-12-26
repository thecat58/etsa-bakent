from pathlib import Path
import os
from dotenv import load_dotenv
import environ


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-default-key')  # Valor por defecto para desarrollo

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Inicializar django-environ
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Application definition
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'whitenoise.runserver_nostatic',
    'django_seed',
    'principal',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "django.middleware.security.SecurityMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings (allow only localhost in development)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',  # Asegúrate de que tu frontend esté corriendo en este puerto
]

CORS_ALLOW_METHODS = [
    'POST',
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'x-csrftoken',
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-requested-with',
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'bakentetsa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bakentetsa.wsgi.application'

# Database configuration for local development (use SQLite by default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

# Password validation
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

AUTH_USER_MODEL = 'principal.Usuario'

# Internationalization
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Bogota'  # Establecer la zona horaria local para Colombia

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Allowed Hosts for local development
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Static file storage (only needed if using Whitenoise for production)
# Can be left as default in local development
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # Para producción si decides usar Whitenoise

# CSRF trusted origins (local development, no need to modify unless using cookies)
CSRF_TRUSTED_ORIGINS = ['https://localhost:8000']  # Si estás trabajando con un frontend en Angular o React en localhost
