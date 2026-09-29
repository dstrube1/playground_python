from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobForm
from .models import Job


def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save()
            # This import is in this function to make its purpose more obvious,
            # and because I'm still learning.
            from .tasks import process_job
            process_job.delay(job.id)
            # Old
            #return redirect("job_created")
            # New
            return redirect("job_detail", job_id=job.id)
    else:
        form = JobForm()

    return render(
        request,
        "jobs/create_job.html",
        {"form": form},
    )


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    return render(
        request,
        "jobs/job_detail.html",
        {"job": job},
    )


def job_status(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    return JsonResponse({
        "status": job.status,
        "result": job.result,
        "completed_at": job.completed_at,
    })


def job_created(request):
    return render(request, "jobs/job_created.html")