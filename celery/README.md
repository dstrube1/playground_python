```
celery-django-demo/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── celery.py
├── jobs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── tasks.py
└── templates/
    └── jobs/
```
    
```
Job:
 ├── id
 ├── input_text
 ├── status
 ├── result
 ├── created_at
 └── completed_at
Example Job:
id:           17
input_text:   "The quick brown fox..."
status:       SUCCESS
result:       "Characters: 43, words: 9"
created_at:   2026-09-25 10:52
completed_at: 2026-09-25 10:52
```

Getting started, from celery-django-demo:
```
# Setup the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install and verify django
pip install django
python -m django --version

# Create the django project
django-admin startproject config .

# Start django (Ctrl+C to stop)
python manage.py runserver

# Apply migrations (this also creates the default SQLite database)
python manage.py migrate

# Create the jobs app
python manage.py startapp jobs

# SIDENOTE:
config is our Django project — configuration for the overall website/application.
jobs is a Django application — a self-contained piece of functionality within the project.
# END SIDENOTE

# Next, updated config/settings.py & jobs/models.py
# Then, tell Django to generate a migration for the Job model
python manage.py makemigrations

# Apply the new model (add Job table in SQLite)
python manage.py migrate

# Update jobs/admin.py, then add an admin user
python manage.py createsuperuser
Username: admin
Email address: a@b.com
Password: admin
Password (again): admin

# Start server
python manage.py runserver

# Go to and verify login and Jobs
http://127.0.0.1:8000/admin/

# Next, create and implement jobs/forms.py and update jobs/views.py
# Then, create the templates
mkdir -p jobs/templates/jobs

# Create and fill out 
jobs/templates/jobs/create_job.html
jobs/templates/jobs/job_created.html
jobs/urls.py

# Update
config/urls.py

# Goto and verify
http://127.0.0.1:8000/jobs/
http://127.0.0.1:8000/admin/jobs/job/

# Install celery & verify
pip install celery
celery --version

# Install redis
brew install redis

# Add Docker to $PATH & verify
echo 'export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
docker --version

# Start redis via docker
docker run -d \
  --name celery-redis \
  -p 6379:6379 \
  redis:7

# Verify Docker is running redis
docker ps

# Create and populate config/celery.py
# Update config/__init__.py
# Update config/settings.py

# Install & verify the Python Redis connector
pip install redis
python -c "import redis; print(redis.__version__)"

# Verify that Django → Celery → Redis is configured correctly
celery -A config worker --loglevel=INFO

# Create and implement jobs/tasks.py
# Stop (Ctrl+C) and rerun celery and confirm the output includes this:
#[tasks]
#  . jobs.tasks.process_job
celery -A config worker --loglevel=INFO --pool=solo
# Note: `--pool=solo` option: the default multiprocessing pool ran into a Billiard/Celery worker-process issue, while the solo pool works correctly.

# Open a new terminal window / tab, go to this project's directory (if not already there) 
# and run the Django shell
python manage.py shell
from jobs.tasks import process_job
result = process_job.delay(123)

# Confirm celery worker output is something like this:
#[... INFO/MainProcess] Task jobs.tasks.process_job[...] received
#[... WARNING/MainProcess] Processing job 123...
#[... WARNING/MainProcess] Finished job 123.
#[... INFO/MainProcess] Task jobs.tasks.process_job[...] succeeded in 5.001800318947062s: 'Job 123 completed'

# Connect the task to the Job model:
# Update jobs/tasks.py (compare V1 to V2)
# Restart the celery worker
# Create a test Job:
# From the Django shell:
from jobs.models import Job
job = Job.objects.create(input_text="Hello from Celery")
# Verify job object was created
job
# then 
from jobs.tasks import process_job
result = process_job.delay(job.id)
# Verify in celery worker:
#Task jobs.tasks.process_job[...] received
#Processing job 1...
#Finished job 1.
#Task jobs.tasks.process_job[...] succeeded ...
# then in Django shell
job.refresh_from_db()
job.status
job.result
job.completed_at


```

















































