from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
