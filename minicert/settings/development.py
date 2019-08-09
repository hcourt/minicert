# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mj2!x*acf8y8zzm)2d7(tt)3hby6kk+i#*h3e@746ygsd8kfd6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}

ACTIVATE_AUTHORITY = 'http://0.0.0.0:80/post'
