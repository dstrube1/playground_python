from .celery import app as celery_app

# Make sure the Celery application is loaded when Django loads the config package
__all__ = ("celery_app",)