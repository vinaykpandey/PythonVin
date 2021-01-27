

In bash shell,when run command: celery beat -A proj -l info, only send to queue, not runing the task,
but change the command celery worker -A proj -l info, the task will trigger.
Beat does not execute tasks, it just sends the messages. You need both a beat instance and a worker instance!s
For running periodic tasks you have to run two services: celery beat together with celery worker.

https://stackoverflow.com/questions/42566322/celery-worker-and-beat-load-in-one-command

celery -A periodic_task_v2 worker --beat --loglevel=info

#celery -A periodic_task_v1 beat --loglevel=info
#celery -A periodic_task_v1 worker -B --loglevel=info  # case 1

# celery worker -h
# celery -A periodic_task_v2 beat --loglevel=info
# celery -A periodic_task_v2 beat -l debug
# celery -A periodic_task_v2 worker -B --loglevel=info  # case 1
# celery -A periodic_task_v2 worker -l --loglevel=info

# celery-worker-and-beat-load-in-one-command
celery -A periodic_task_v2 worker --beat --loglevel=info
OR
celery -A periodic_task_v2 worker -B --loglevel=info