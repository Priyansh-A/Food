from decouple import config 
from .base import *

DEBUG = False

ADMINS = [
    ('admin', 'admin101@gmail.com'),
]

ALLOWED_HOSTS = ['localhost','127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB', default='postgres'),
        'USER': config('POSTGRES_USER', default='postgres'),
        'PASSWORD': config('POSTGRES_PASSWORD', default='postgres'),
        'HOST': config('POSTGRES_HOST',default='db'),
        'PORT': config('POSTGRES_PORT',default='5432')
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

REDIS_HOST = config('REDIS_HOST', default='cache')
REDIS_PORT = config('REDIS_PORT', default=6379)
REDIS_DB = config('REDIS_DB', default=0)
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
