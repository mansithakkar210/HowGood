"""
Django settings for HowGood project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zdv!@zf_moo!m4%tbdz*z8hqi#93ce1%b*x=mv1%eb=m1xo+_u'

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
	'HowGoodApp'
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

ROOT_URLCONF = 'HowGood.urls'

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

WSGI_APPLICATION = 'HowGood.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
		'OPTIONS': {
            'options': '-c search_path=pcp'
        },
        'NAME': 'mansi',
        'USER': 'postgres',
        'PASSWORD': 'js0I6RUW1MkUaGrc3xvz',
        'HOST': 'cosmetics.ci9ebgbniz3t.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
		},
		
	#'howgood_pcp_data': {
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'howgood_pcp',
        #'USER': 'postgres',
        #'PASSWORD': 'js0I6RUW1MkUaGrc3xvz',
        #'HOST': 'cosmetics.ci9ebgbniz3t.us-east-1.rds.amazonaws.com',
        #'PORT': '5432',
		#}
}

def decide_on_model(model):
	return 'howgood_pcp_data' if model._meta.app_label == 'HowGoodApp' else None
	
class HowGoodDbRouter:
	def db_for_read(self, model, **hints):
		return decide_on_model(model)

	def db_for_write(self, model, **hints):
		return decide_on_model(model)
		
	def allow_relation(self, obj1, obj2, **hints):
        # Allow any relation if both models are part of the worlddata app
		if obj1._meta.app_label == 'HowGoodApp' and obj2._meta.app_label == 'HowGoodApp':
			return True
        # Allow if neither is part of worlddata app
		elif 'HowGoodApp' not in [obj1._meta.app_label, obj2._meta.app_label]:
			return True
	def allow_migrate(self, db, app_label, model_name=None, **hints):
        # allow migrations on the "default" (django related data) DB
		if db == 'default' and app_label != 'HowGoodApp':
			return True
		if db == 'howgood_pcp_data' and app_label == "HowGoodApp":
			return True

		return False


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
