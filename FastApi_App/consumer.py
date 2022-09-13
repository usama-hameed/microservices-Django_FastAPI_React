import pika

# amqps://bescccok:rsjlBxeksDvwcp23H0QDJh83qttksbsF@sparrow.rmq.cloudamqp.com/bescccok

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
