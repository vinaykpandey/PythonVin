import time
import logging
from celery import Celery, shared_task

# BROKER_URL = 'redis://localhost:6379/0'
# app = Celery('tasks', broker=BROKER_URL)

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('hello', broker=BROKER_URL, backend=BACKEND_URL)

logging.basicConfig(filename="celery_math_cal.log", level=logging.DEBUG)

# app.autodiscover_tasks()
@app.task
def welcome():
    print("welcome  task is executed")
    logging.debug("welcome  task is executed")
    for i in range(50):
        time.sleep(1)
        print("welcome loop count: " + str(i))
        logging.debug("welcome loop count: " + str(i))

@app.task
def add(x, y):
    logging.debug("Add  task is executed {0} {1}".format(x, y))
    print("Add  task is executed x is ", x, "y is: ", y)
    sum = x+y
    print("Sum is: " + str(sum))
    logging.debug("Sum is: " + str(sum))
    # return sum # it doesn't make any sense in real

@shared_task
def multiply(x, y):
    print("Multiplication  task is executed")
    logging.debug("Multiplication  task is executed")
    multiplication = x * y
    print("Multiplication is: " + str(multiplication))
    logging.debug("Multiplication is: " + str(multiplication))
    # return multiplication # it doesn't make any sense in real


