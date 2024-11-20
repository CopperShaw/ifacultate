import os

from dotenv import load_dotenv

from .base import *

# Load environment variables
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(" ")

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# SMTP Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = "True"

EMAIL_HOST_USER = "learn.cortex@gmail.com"
EMAIL_HOST_PASSWORD = os.getenv("DJANGO_GMAIL_PASSWORD")

DEFAULT_FROM_EMAIL = "learn.cortex@gmail.com"

# for prod
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.purelymail.com"
# EMAIL_PORT = "465"
# EMAIL_USE_SSL = "True"

# EMAIL_HOST_USER = "noreply@ifacultate.ro"
# EMAIL_HOST_PASSWORD = os.getenv("DJANGO_PURELYMAIL_PASSWORD")

# DEFAULT_FROM_EMAIL = "noreply@ifacultate.ro"
