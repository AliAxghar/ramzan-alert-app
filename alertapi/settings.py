"""
Django settings for alertapi project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+zjjga&0_&6^dbvv(56&48)v9e5l2gll#3o=nsb+j*v(dz)-m8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'fcm_django',
    'django_crontab',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alertapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'alertapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ramzan_alert',
#         'USER' : 'postgres',
#         'PASSWORD' :'1234',
#         'HOST' : 'localhost'

#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ramzan_alert',
        'USER' : 'frienddoouser',
        'PASSWORD' :'GAL6615M13',
        'HOST' : 'localhost'

    }
}

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES' :('rest_framework.permissions.IsAuthenticatedOrReadOnly',)
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
) 
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



# PUSH_NOTIFICATIONS_SETTINGS = {
#         "FCM_API_KEY": "AAAAFcIN8dc:APA91bHTpwD7cr2c4NK-haqi0TFffWznJNzZnR_VffT_VSNhaQDJBqNEFMd4bw1wITMOMWRSfKORYkQG95O6r_6XhvVxL-3RYxVRExrcBaVnbYpaOiOVHfkKXX_SDNmLELOzehOI7a7z",
#         "FCM_POST_URL": "https://fcm.googleapis.com/fcm/send",
#         "FCM_MAX_RECIPIENTS": 1000,
#         "DELETE_INACTIVE_DEVICES": False,
#         "ONE_DEVICE_PER_USER": True,
# }

FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "AAAAFcIN8dc:APA91bHTpwD7cr2c4NK-haqi0TFffWznJNzZnR_VffT_VSNhaQDJBqNEFMd4bw1wITMOMWRSfKORYkQG95O6r_6XhvVxL-3RYxVRExrcBaVnbYpaOiOVHfkKXX_SDNmLELOzehOI7a7z",
        # "FCM_POST_URL": "https://fcm.googleapis.com/fcm/send",
        # "FCM_MAX_RECIPIENTS": 1000,
        # "DELETE_INACTIVE_DEVICES": False,
        # "ONE_DEVICE_PER_USER": True,
}
CRONJOBS = [
    ('0 0 * * *', 'api.cron.run')
]




