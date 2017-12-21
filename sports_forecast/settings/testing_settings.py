import logging
import os

from .settings import CACHES, DATABASES, BASE_DIR

# Django automatically sets DEBUG = False when running tests

logging.disable(logging.CRITICAL)

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['*']

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'testdb.sqlite3'),
}

CACHES['default'] = {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
