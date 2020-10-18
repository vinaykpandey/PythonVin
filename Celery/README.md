pip install celery==4.3.0

Installing collected packages: pytz, billiard, vine, more-itertools, zipp, importlib-metadata, amqp, kombu, celery

pip install redis==3.3.11
Installing collected packages: redis
Successfully installed redis-3.3.11




celery -A tasks worker --loglevel=info


python, celery, redis(pub sub) # publisher subscribers
