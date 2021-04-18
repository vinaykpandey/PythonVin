from celery import Celery

# BROKER_URL = 'redis://localhost:6379/0'
# app = Celery('tasks', broker=BROKER_URL)

BROKER_URL = 'pyamqp://guest:guest@localhost://'
BACKEND_URL = 'redis://localhost:6379/1'
CELERY_ROUTES = {
    'receiver.tasks': {'queue': 'Add'},
}
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)
app.send_task('receiver.add', args=(33, 4))

# https://medium.com/@mannemvamsi/running-celery-workers-for-specific-task-queues-19e6dd3febff
