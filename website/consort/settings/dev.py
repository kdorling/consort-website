from .base import *

import os


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=1))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", default="django-insecure-csov7al8s0(4^!6)pfzh$kc8wd(#smvj&679u()mo22ia9_v4!")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="localhost 127.0.0.1 [::1]").split(" ")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

try:
    from .local import *
except ImportError:
    pass
