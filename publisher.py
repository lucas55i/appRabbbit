import pika
import json
from rabbit import RabbitmqConnection

connection = RabbitmqConnection()


class PublisherMQ:
    def __init__(self) -> None:
        self.exchange = "app_exchange"
        self.routing_key = ""
        self.body = {"Nome": "Lucas silva"}

    def send_message(self):
        connection.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=json.dumps(self.body),
            properties=pika.BasicProperties(delivery_mode=2),
        )


publisher = PublisherMQ()
publisher.send_message()
