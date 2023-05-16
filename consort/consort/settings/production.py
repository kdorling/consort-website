from .base import *

DEBUG = False
SECRET_KEY = "c^c7ycg_9)vzu+$k4w*=e9pa2vcl0cpu-a2!sfk5p5v5@5nxh#"
ALLOWED_HOSTS = ["localhost", "138.197.131.37"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "consort_db",
        "USER": "admin",
        "PASSWORD": "conSort2023sql",
        "HOST": "localhost",
        "PORT": "",
    }
}

try:
    from .local import *
except ImportError:
    pass
