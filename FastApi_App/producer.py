import pika
import json
# amqps://bescccok:rsjlBxeksDvwcp23H0QDJh83qttksbsF@sparrow.rmq.cloudamqp.com/bescccok


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)


channel = connection.channel()

channel.queue_declare(queue='admin')


def publish(method, body):
    properties = pika.BasicProperties(method)
    body = bytes(body)
    channel.basic_publish(exchange='', routing_key='admin', body=body, properties=properties)


channel.close()
