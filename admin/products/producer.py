import pika
import json
import os
# amqps://bescccok:rsjlBxeksDvwcp23H0QDJh83qttksbsF@sparrow.rmq.cloudamqp.com/bescccok


connection = pika.BlockingConnection(
    pika.ConnectionParameters(os.getenv('AMPQ_DSN'))
)


channel = connection.channel()

channel.queue_declare(queue='main')


def publish(method, body):
    properties = pika.BasicProperties(method)
    # body = bytes(body)
    channel.basic_publish(exchange='', routing_key='main', body=body, properties=properties)


channel.close()
