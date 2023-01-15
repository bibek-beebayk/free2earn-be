from be.settings.base import BASE_DIR

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