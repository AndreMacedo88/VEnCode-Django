from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# If DEBUG is False, send the errors to the email:
ADMINS = [
    ('Andre', 'andre.lopes.macedo@gmail.com'),
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'VEnCode_Django.urls'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': '',
        'HOST': config("DB_HOST"),
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configure Django App for Heroku.
django_heroku.settings(locals())

# Production set up for heroku:
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Allauth configurations, backend to send sign-in e-mail verification e-mail:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# REDIS related settings
CELERY_BROKER_URL = config('REDIS_URL', default="redis://")
CELERY_RESULT_BACKEND = config('REDIS_URL', default="redis://")
BROKER_URL = config('REDIS_URL', default="redis://")

# Allauth related settings
EMAIL_HOST = config("MAILGUN_SMTP_SERVER")
EMAIL_PORT = config("MAILGUN_SMTP_PORT")
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = config("MAILGUN_SMTP_LOGIN")
EMAIL_HOST_PASSWORD = config("MAILGUN_SMTP_PASSWORD")
