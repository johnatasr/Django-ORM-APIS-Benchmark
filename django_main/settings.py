import os
BASE_DIR = os.path.abspath(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'DATABASE': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432
    }
}


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_main.apps.DjangoMainConfig',
    )

SECRET_KEY = 'jsd9sdyo78dTQ2G3HL2QMP9qjoj2dodimqpSCDu'
