from django.urls import path

from . import views


urlpatterns = [
    path("", views.create_job, name="create_job"),
    path("created/", views.job_created, name="job_created"),
]