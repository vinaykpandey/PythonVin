from celery import Celery, Task

BROKER_URL = 'pyamqp://guest:guest@localhost://'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

# app.autodiscover_tasks()
@app.task
def welcome(msg_str):
    print("welcome  task is executed {0}".format(msg_str))


# celery -A welcome worker --loglevel=info -Q TestSample