from django.urls import path

from . import views


urlpatterns = [
    path("", views.create_job, name="create_job"),
    path("created/", views.job_created, name="job_created"),
    path("<int:job_id>/", views.job_detail, name="job_detail"),
    path("<int:job_id>/status/", views.job_status, name="job_status"),
]