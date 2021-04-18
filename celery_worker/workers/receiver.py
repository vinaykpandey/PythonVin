from celery import Celery

# BROKER_URL = 'redis://localhost:6379/0'
# app = Celery('tasks', broker=BROKER_URL)

BROKER_URL = 'pyamqp://guest:guest@localhost://'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


@app.task
def add(x, y):
    print("result is: ", x + y)
    return x + y

# celery worker -l info -A receiver
