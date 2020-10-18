import time
from celery import Celery, shared_task
from functions import file_write
# BROKER_URL = 'redis://localhost:6379/0'
# app = Celery('tasks', broker=BROKER_URL)

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)
# app.autodiscover_tasks()

@shared_task
def welcome():
    print("Welcome  task is executed")
    file_write("Welcome  task is executed")
    for i in range(50):
        # time.sleep(1.5)
        print("Welcome loop count: " + str(i))
        file_write("Welcome loop count: " + str(i))
    print("Welcome End")
    file_write("Welcome End")
    # return multiplication # it doesn't make any sense in real

@app.task
def add(x, y):
    print("Add  task is executed")
    file_write("Add  task is executed")
    for i in range(50):
        # time.sleep(1)
        print("Add loop count: " + str(i))
        file_write("Add loop count: " + str(i))
    sum =  x + y
    print("Sum is: "+ str(sum))
    file_write("Sum is: "+ str(sum))
    # return sum # it doesn't make any sense in real

@shared_task
def multiply(x, y):
    print("Multiplication  task is executed")
    file_write("Multiplication  task is executed")
    for i in range(50):
        # time.sleep(2)
        print("Multiplication loop count: " + str(i))
        file_write("Multiplication loop count: " + str(i))

    multiplication =  x * y
    print("Multiplication is: "+ str(multiplication))
    file_write("Multiplication is: " + str(multiplication))
    # return multiplication # it doesn't make any sense in real