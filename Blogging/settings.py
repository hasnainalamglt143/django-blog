"""
Django settings for Blogging project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# getting hidden variables

# SECRET_KEY="hqhd+-u8$#25db0%=ik8j#*v8yv%$dwhny=k9=6tdc%+%5h^w$"

SECRET_KEY=os.getenv("SECRET_KEY")
print(SECRET_KEY)
# Environment=os.getenv("ENVIROMENT",default="production")
Environment=os.getenv("Enviroment","development")

# SECURITY WARNING: don't run with debug turned on in production!
if Environment=="development" :
        DEBUG = True
else:
      DEBUG = False  

ALLOWED_HOSTS = [".vercel.app"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    
     'tailwind',
     'blog',
     'django_browser_reload',
     'ckeditor',
    'ckeditor_uploader',
     
    
    
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
      "django_browser_reload.middleware.BrowserReloadMiddleware",

]

ROOT_URLCONF = 'Blogging.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'blog/templates')],
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

WSGI_APPLICATION = 'Blogging.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# import pymysql

# pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
          
    "ENGINE": "django.db.backends.mysql",
        "NAME": "blogging",
        "USER": "root",
        "PASSWORD": os.getenv("_password"),
        "HOST": "127.0.0.1",
        "PORT": "3306",

    }
      
         
    

}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
#media root

MEDIA_URL = 'blog/profiles_pic/'
if DEBUG:
    MEDIA_ROOT = BASE_DIR /'blog'/'profiles_pic'
else:
      CLOUDINARY_STORAGE = {
            'CLOUDINARY_URL':os.getenv("CLOUDINARY_URL")}
      DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Ensure you have the following in your urls.py





# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT=os.path.join(BASE_DIR,"staticfiles_dir")
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "blog/static_src"),
    os.path.join(BASE_DIR, "blog/static"),


    # Add any other static directories here
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
TAILWIND_APP_NAME ='blog'
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"






# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hasnainalamglt143@gmail.com'
EMAIL_HOST_PASSWORD = ""
# DEFAULT_FROM_EMAIL = 'your_email@gmail.com'


# //configuratin for editor

CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 820,
    },
    'extraplugins':["links"]
}

