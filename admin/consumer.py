import pika
from admin.products.models import Product
# amqps://bescccok:rsjlBxeksDvwcp23H0QDJh83qttksbsF@sparrow.rmq.cloudamqp.com/bescccok

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()


def callback(ch, method, properties, body):
    import json
    print('Received in admin')
    id = json.loads(body)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    print("Product Liked!!! ")


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
