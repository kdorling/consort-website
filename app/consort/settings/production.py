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


# Email settings

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "kdor.trades@gmail.com"
EMAIL_HOST_PASSWORD = "wxogvujbevzpxbgj"


# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

try:
    from .local import *
except ImportError:
    pass
