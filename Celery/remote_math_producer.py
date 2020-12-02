from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('hello', broker=BROKER_URL, backend=BACKEND_URL)
app = Celery("workers")


app.conf.task_routes = {
   {'queue': 'remote_queue'}
}