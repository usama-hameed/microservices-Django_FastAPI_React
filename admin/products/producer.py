import pika

# amqps://bescccok:rsjlBxeksDvwcp23H0QDJh83qttksbsF@sparrow.rmq.cloudamqp.com/bescccok


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)


channel = connection.channel()

channel.queue_declare(queue='main')


def publish():
    channel.basic_publish(exchange='', routing_key='main', body=b'hello')


channel.close()
