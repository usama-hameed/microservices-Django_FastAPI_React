import pika
from .models import Product
from fastapi_sqlalchemy import db

import json

# amqps://bescccok:rsjlBxeksDvwcp23H0QDJh83qttksbsF@sparrow.rmq.cloudamqp.com/bescccok

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body.decode('utf-8'))
    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
