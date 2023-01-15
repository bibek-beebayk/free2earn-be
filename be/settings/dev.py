from be.settings.base import BASE_DIR

SECRET_KEY = 'django-insecure-z@!sh63p7)a56uox7-o9)61a=@j^_=1)a_jzd5$9sap^$6)8my'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'free2earn',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': '',
#         'PORT': ''
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}