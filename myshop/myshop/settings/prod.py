from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-j^l9w5b@39wl#hx6wua3(vscie+d3_4#aqw(qynv4z@!3b8+xq'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myshop',
        'USER': 'sergey',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432',
    }
}