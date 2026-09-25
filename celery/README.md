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
```





























