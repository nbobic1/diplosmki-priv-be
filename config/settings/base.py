import os
from datetime import timedelta
from pathlib import Path
from google.oauth2 import service_account

from storages.backends.gcloud import GoogleCloudStorage

import environ


BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = environ.Path(__file__) - 3
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    env.read_env(str(ROOT_DIR.path(".env")))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!rpxk1f6ru8%qxu*-7p0^b16x%t!v1^0^se3i^#vhs&(z!(#kg"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
WSGI_APPLICATION = 'vercel_app.wsgi.app'
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "storages",
    "django_cleanup.apps.CleanupConfig",
    "rest_framework_simplejwt.token_blacklist",
    "drf_yasg",
]

LOCAL_APPS = [
    "core.apps.CoreServiceConfig",
]
INSTALLED_APPS += LOCAL_APPS

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":  ['rest_framework_simplejwt.authentication.JWTAuthentication'],
}

AUTH_USER_MODEL = "core.User"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "TOKEN_OBTAIN_SERIALIZER": "core.serializers.CustomTokenObtainPairSerializer",
}

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware"
]

ROOT_URLCONF = "config.urls"
CORS_ALLOW_ALL_ORIGINS = True

MIGRATION_MODULES = {
    "core": "core.migrations"
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

POSTGRES_DB = "diplomski"
POSTGRES_SCHEMA = env("POSTGRES_SCHEMA", default="public")
POSTGRES_USER ="diplomski_user"
POSTGRES_PASSWORD = "Z0BCpUoSsSzlGvhcaJYNMYXeWctkalTY"
POSTGRES_HOST ="dpg-cir9tftph6ev5rfn3v90-a" 
POSTGRES_PORT = 5432


DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': {
                'options': f'-c search_path={POSTGRES_SCHEMA}'
            },
            'NAME': POSTGRES_DB,
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': POSTGRES_HOST,
            'PORT': POSTGRES_PORT
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# GCS config
DEFAULT_FILE_STORAGE = 'config.settings.base.Media'

GS_BUCKET_NAME = 'diplomski_django'

GS_FILE_OVERWRITE = True

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(ROOT_DIR, 'envs/diplomski-383408-4e3632d3176d.json'),
)

Media = lambda: GoogleCloudStorage(location='media')

