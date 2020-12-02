pip install celery==4.3.0

Installing collected packages: pytz, billiard, vine, more-itertools, zipp, importlib-metadata, amqp, kombu, celery

pip install redis==3.3.11
Installing collected packages: redis
Successfully installed redis-3.3.11


celery -A tasks worker --loglevel=info

python, celery, redis(pub sub) # publisher subscribers


flower
https://flower.readthedocs.io/en/latest/install.html

flower -A task --port=5555

How to keep multiple independent celery queues?
https://stackoverflow.com/questions/19853378/how-to-keep-multiple-independent-celery-queues

error:
Last version of vine is 5.0.0 and fresh push was in 06.09.2020 (yesterday) :), and this version do not have any five.py file. So downgrade vine version to.

vine==1.3.0

works for me

ImportError: cannot import name 'Command' from 'celery.bin.base'
https://stackoverflow.com/questions/64180054/importerror-cannot-import-name-command-from-celery-bin-base


How to keep multiple independent celery queues?
https://stackoverflow.com/questions/19853378/how-to-keep-multiple-independent-celery-queues

Running multiple workers using Celery
https://serverfault.com/questions/655387/running-multiple-workers-using-celery

Celery - run different workers on one server
https://stackoverflow.com/questions/5463241/celery-run-different-workers-on-one-server

https://github.com/celery/celery/issues/3911
celery -A project worker -l info --concurrency=3 --beat -E

solo
https://www.distributedpython.com/2018/10/26/celery-execution-pool/


https://docs.celeryproject.org/en/stable/userguide/tasks.html
add.name

https://github.com/celery/celery


VERY USEFUL BLOG
______________________________________________________________
https://tests4geeks.com/blog/python-celery-rabbitmq-tutorial/

celery async: rabbitmq as broker and redis as results backend
----------------------------------------------------------------
https://doordash.engineering/2020/09/03/eliminating-task-processing-outages-with-kafka/
https://towardsdatascience.com/serving-deep-learning-algorithms-as-a-service-6aa610368fde

# celery -A workers.math_cal worker --loglevel=info

# celery -A proj worker -l info -Q queue1
# celery -A proj worker -l info -Q queue2

# celery -A workers.math_cal worker --loglevel=info -Q math_cal1
# celery -A workers.math_cal worker --loglevel=info -Q math_cal2