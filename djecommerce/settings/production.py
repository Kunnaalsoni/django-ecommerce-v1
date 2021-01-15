from .base import *

DEBUG = config('DEBUG', cast=bool)
# ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

# STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')