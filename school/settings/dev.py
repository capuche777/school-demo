from .base import *

SECRET_KEY = '3@(2#f78$ima@91y04uhqy*r6c98syn+79xff2=6^6f-b9_5=a'
DEBUG = True
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ('127.0.0.1')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Taks for every hour
CRONJOBS = [
    ('* 6 * * *', 'core.cron.my_cron_job')
]

CRONTAB_DJANGO_SETTINGS_MODULE = 'school.settings.dev'
