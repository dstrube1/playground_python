from django.shortcuts import redirect, render

from .forms import JobForm


def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save()
            # This import is in this function to make its purpose more obvious,
            # and because I'm still learning.
            from .tasks import process_job
            process_job.delay(job.id)
            return redirect("job_created")
    else:
        form = JobForm()

    return render(
        request,
        "jobs/create_job.html",
        {"form": form},
    )


def job_created(request):
    return render(request, "jobs/job_created.html")