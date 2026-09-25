# celery/tasks.py

# from:
#https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#first-steps

from celery import Celery

app = Celery('tasks', # the name of the current module
 broker='pyamqp://guest@localhost//') # the broker keyword argument,
 # specifying the URL of the message broker you want to use

@app.task
def add(x, y):
    return x + y

# celery -A tasks worker --loglevel=INFO
