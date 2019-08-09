from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-here'

# Certificate authority to contact when activating and deactivating certificates
ACTIVATE_AUTHORITY = 'http://0.0.0.0:80/post'

ALLOWED_HOSTS = ['*']
