from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-here'

# Certificate authority to contact when activating and deactivating certificates
ACTIVATE_AUTHORITY = 'http://httpbin:80/post'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',  # set in docker-compose.yml
        'PORT': 5432  # default postgres port
    }
}

ALLOWED_HOSTS = ['*']
