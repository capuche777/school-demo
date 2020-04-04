from .base import *
from decouple import config, Csv


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'etc/mysql/demo1-mysql.cnf',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Taks for every hour
CRONJOBS = [
    ('0 0 * * *', 'core.cron.my_cron_job')
]

CRONTAB_DJANGO_SETTINGS_MODULE = 'school.settings.production'

STATIC_ROOT = '/home/jeremias/public_html/demo1/static'
MEDIA_ROOT = '/home/jeremias/public_html/demo1/media'

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
