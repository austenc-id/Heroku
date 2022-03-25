from pathlib import Path
import os

# third party imports
import django_heroku


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-q3124893v3&)s3*f#^3!lcn)^!2$(0l#7qw8=i65hw+^h@%k^7'

DEBUG = True

ALLOWED_HOSTS = [
    "acmf-resume.herokuapp.com"
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # project apps
    '_home',
    '_bio',
    '_work',
    # '_education',
    # '_skills',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / '_assets/templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d6hovsvqnp7hv5",
        "USER": "nlxbkwxffbspsm",
        "PASSWORD": "a1ae3411a6059decb9264046f2eec7d47a2941ffbb9b82c96fab302db42b1903",
        "HOST": "ec2-44-194-167-63.compute-1.amazonaws.com",
        "PORT": "5432",
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Anerica/Denver'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = os.path.join(BASE_DIR, '_assets')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())
