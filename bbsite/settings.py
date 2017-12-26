"""
Django settings for bbsite project.

Generated by 'django-admin startproject' using Django 1.11.6.

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
SECRET_KEY = '3we6-v1vo=ad7_hfes8@fl%h+yi532$tzh%ovm_real91+sud1'

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
    'bbs01',
    # 'django.contrib.comment',
    #  'django.contrib.sites',
]

MIDDLEWARE_CLASSES  = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bbsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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





WSGI_APPLICATION = 'bbsite.wsgi.application'
# SITE_ID=1

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bbsite',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


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

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/



# HERE = os.path.dirname(__file__)
# STATICFILES_DIRS = (
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
#     HERE+STATIC_URL,
# )
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
#
# STATICFILES_DIRS = (
#     ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),
#     ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ),
#     ('fonts',os.path.join(STATIC_ROOT,'fonts').replace('\\','/') ),
#     ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ),
# )
# STATIC_URL = '/static/'


# # add 这步的意思就是，在网站项目的根目录下，有一个templates文件夹，里面放置所有的模板
# TEMPLATE_DIRS = (
#     os.path.join(os.path.dirname(__file__), '../templates').replace('\\','/'),
# )
#
#
# STATIC_PATH= os.path.join(os.path.dirname(__file__), '../static').replace('\\','/')

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates')
# )
#
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

#
# TEMPLATE_DIRS = [
#     {
#         os.path.join(BASE_DIR, 'templates'),
#     },
# ]
#
#
# STATICFILES_DIRS = [
#     {
#         os.path.join(BASE_DIR, 'static'),
#     },
# ]
