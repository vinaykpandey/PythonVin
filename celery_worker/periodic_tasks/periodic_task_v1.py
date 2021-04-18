from celery import Celery
from celery.schedules import crontab
import logging

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

logging.basicConfig(filename="periodic_task_v1", level=logging.DEBUG)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds. case 1
    sender.add_periodic_task(
        2.0,
        test.s('hello'),
        name='add every 2'
    )

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


@app.task
def test(arg):
    print("Celery beat is running----")
    logging.debug("Celery beat is running----")
    print(arg)
