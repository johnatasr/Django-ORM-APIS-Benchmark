import os
BASE_DIR = os.path.abspath(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django_main.db.backends.postgresql',
        'NAME': 'postgres',
        'DATABASE': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432
    }
}


INSTALLED_APPS = (
    'django_main.contrib.auth',
    'django_main.contrib.contenttypes',
    'db.apps.DbConfig',
    )

SECRET_KEY = 'jsd9sdyo78dTQ2G3HL2QMP9qjoj2dodimqpSCDu'
