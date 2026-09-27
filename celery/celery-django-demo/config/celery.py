import os

from celery import Celery

# Tell Celery which Django settings module to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Tell Celery to read its configuration from Django's settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Tell Celery to look through installed Django apps for tasks.py files
app.autodiscover_tasks()