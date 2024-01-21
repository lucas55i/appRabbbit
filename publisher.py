import pika
import json

dado = {"Nome": "Lucas silva"}


connection = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(username="guest", password="guest"),
)


channel = pika.BlockingConnection(connection).channel()
channel.basic_publish(
    exchange="app_exchange",
    routing_key="",
    body=json.dumps(dado),
    properties=pika.BasicProperties(delivery_mode=2),
)
