from .base import *

SECRET_KEY = 'django-insecure-#_w*t$q_828v(h536v=jg=q3$j8)%+7969s2*a52a1kh*41-dc'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}