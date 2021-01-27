#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='TestSample')
channel.basic_publish(exchange='',
                      routing_key='vinay_test',
                      body='Hello World!')
print (" [x] Sent 'Hello World!'")