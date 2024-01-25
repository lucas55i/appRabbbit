from rabbit import RabbitmqConnection
import logging

rabbitmq_connection = RabbitmqConnection()


class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self.queue = "app_queue"
        self.callback = callback
        self.channel = rabbitmq_connection.channel
        self.connect_queue()

    def connect_queue(self):  # TODO possivel refatoração
        self.channel.queue_declare(
            queue=self.queue,
            durable=True,
        )

        self.channel.basic_consume(
            queue=self.queue, auto_ack=True, on_message_callback=self.callback
        )

        return self.channel

    def start(self):
        print(f"listen RabbitMQ on Port 5672")
        self.channel.start_consuming()


def minha_callback(ch, method, properties, body):
    print(body)


rabbitmq_consumer = RabbitmqConsumer(minha_callback)
rabbitmq_consumer.start()
