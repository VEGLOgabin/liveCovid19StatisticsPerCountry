"""
Django settings for corona_data_collection_api project.

Generated by 'django-admin startproject' using Django 3.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-np_70^ou^-k7*6n84z1ab7#202+@t0hos!p)g*ddr+q0iy(l(w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_celery_beat",
    "corona_virus_app",
    "account",
    'django_crontab',  #Work very well # If you want to check it , you need just tap this in the shell: less /var/log/cron.log  , in addition, it doesn't need 'python manage.py runserver' before work , just the sys, documentation : https://pypi.org/project/django-crontab/
]

CRONJOBS = [
    # ('0 0 * * *', 'corona_virus_app.cron.write_data_csv_file'),  #WORK VERY WELL
    # ('*/1 * * * *', 'corona_virus_app.cron.write_data_csv_file'),   #WORK VERY WELL
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'corona_data_collection_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath('templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'corona_data_collection_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Porto-Novo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

import os
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from datetime import datetime


#Logs register

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "user_actions_file": {  # Nom du gestionnaire de journal pour les actions de l'utilisateur
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": f"user_actions{datetime.now().strftime('%Y-%m-%d')}.log",  # Nom du fichier de journal pour les actions de l'utilisateur
            "when": "D",  # Rotation quotidienne
            "interval": 1,  # Créez un nouveau fichier chaque jour
            "backupCount": 7,  # Conservez jusqu'à 7 fichiers de journal
            "formatter": "verbose",
        },
    },
    "loggers": {
        "user_actions": {  # Nom du logger pour les actions de l'utilisateur
            "handlers": ["user_actions_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}







CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
AUTH_USER_MODEL = 'account.User'





# from datetime import timedelta
# # from celery.schedules import IntervalSchedule
# from django_celery_beat.models import IntervalSchedule

# from django_celery_beat.models import PeriodicTask, IntervalSchedule
# from myapp.tasks import execute_cron_task  # Import the Celery task function

# # Define an interval schedule for running the task once per day
# interval_schedule, _ = IntervalSchedule.objects.get_or_create(
#     every=1,  # Run the task every 1 day
#     period=IntervalSchedule.DAYS,
# )

# # Create the periodic task
# PeriodicTask.objects.get_or_create(
#     interval=interval_schedule,
#     name="my-task",
#     task="corona_virus_app.tasks.execute_cron_task",  # Specify the Celery task function
# )