"""
Django settings for MatchRecord project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cwotmmzhrqqv#z8%^5ldsb*19wto-6lb0&9r9!j^=j=&g^bhoi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

SECURE_CONTENT_TYPE_NOSNIFF = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nlp_form',
    'orm',
    'render_form',
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

ROOT_URLCONF = 'MatchRecord.urls'

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

WSGI_APPLICATION = 'MatchRecord.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

MOCK_DB = [
    {
        'project_name': 'Save Ganga Project',
        'sponsoring_ministry': 'EF',
        'location_one': 'UP',
        'location_two': 'U',
        'location_three': '',
        'implementation_mode': 'Pr',
        'project_cost': '42',
        'project_description': 'Provide services to reduce pollution and trash to clean river Ganga.'
    },
    {
        'project_name': 'Digital India Programme',
        'sponsoring_ministry': 'DEIT',
        'location_one': 'UP',
        'location_two': '',
        'location_three': '',
        'implementation_mode': 'Pu',
        'project_cost': '500',
        'project_description': 'Provide internet and telecommunication services to every part of the country.'
    }
]

MOCK_FORM_DATA = [
    {
        'project_name': 'Clean Ganga Mission',
        'sponsoring_ministry': 'EF',
        'location_one': 'UP',
        'location_two': 'U',
        'location_three': '',
        'implementation_mode': 'Pr',
        'project_cost': '42',
        'project_description': 'Clean river Ganga by reducing pollution and effusion flowing into its waters.'
    }
]

NON_SUBJECTIVE_KEYS = (
    'sponsoring_ministry',
    'location_one',
    'location_two',
    'location_three',
    'implementation_mode',
    'project_cost',
)

SIMILARITY_CUTOFF = 42