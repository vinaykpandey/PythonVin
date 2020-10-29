from celery import Celery, Task
from celery.schedules import crontab
from functions import file_write
from celery.worker.request import Request


BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

class Person(Task):
    def __init__(self):
        self.name = "Vinay Pandey"

@app.on_after_configure.connect
def setup_periodic_tasks(**kwargs):
    # Calls test('hello') every 10 seconds. case 1
    print("this is step 1")
    app.add_periodic_task(
        2.0,
        test.s('hello'),
        name='add every 2'
    )

    # Calls test('world') every 30 seconds
    #sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


@app.task(bind=True, base=Person)
def test(self, arg):
    print("Celery beat is running----")
    print(arg)
    print(self.__dict__)



"""
# celery worker -h
# celery -A periodic_task_v2 beat --loglevel=info
# celery -A periodic_task_v2 beat -l debug
# celery -A periodic_task_v2 worker -B --loglevel=info  # case 1
# celery -A periodic_task_v2 worker -l --loglevel=info

In bash shell,when run command: celery beat -A proj -l info, only send to queue, not runing the task,
but change the command celery worker -A proj -l info, the task will trigger.
Beat does not execute tasks, it just sends the messages. You need both a beat instance and a worker instance!s
For running periodic tasks you have to run two services: celery beat together with celery worker.

https://stackoverflow.com/questions/42566322/celery-worker-and-beat-load-in-one-command

celery -A periodic_task_v2 worker --beat --loglevel=info
"""