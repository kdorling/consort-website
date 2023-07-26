import os

from .base import *

DEBUG = int(os.environ.get("DEBUG", default=1))
SECRET_KEY =  os.environ.get("SECRET_KEY", "c^c7ycg_9)vzu+$k4w*=e9pa2vcl0cpu-a2!sfk5p5v5@5nxh#")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1").split(" ")


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


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')


try:
    from .local import *
except ImportError:
    pass
