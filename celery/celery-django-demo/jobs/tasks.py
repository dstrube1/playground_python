"""
# V1
# task just prints a message

import time

from celery import shared_task

@shared_task
def process_job(job_id):
    print(f"Processing job {job_id}...")
    time.sleep(5)

    print(f"Finished job {job_id}.")

    return f"Job {job_id} completed"
"""

"""
V2
Now the task interacts with the database:
Job record
   │
   ├── status = PENDING
   │
   ▼
Celery task starts
   │
   ├── status = PROCESSING
   │
   ▼
   wait 5 seconds
   │
   ▼
   ├── result = "Processed: ..."
   ├── status = COMPLETED
   └── completed_at = current time
"""
import time

from celery import shared_task
from django.utils import timezone

from .models import Job


# Tell Celery this function can be executed as a background task
@shared_task
def process_job(job_id):
    job = Job.objects.get(id=job_id)

    print(f"Processing job {job.id}...")

    job.status = "PROCESSING"
    job.save()

	# Give a visible delay so we can actually observe the task being processed asynchronously
    time.sleep(5)

    job.result = f"Processed: {job.input_text}"
    job.status = "COMPLETED"
    # Django's timezone-aware way of getting the current time:
    job.completed_at = timezone.now()
    job.save()

    print(f"Finished job {job.id}.")

    return job.result