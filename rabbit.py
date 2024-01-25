import pika


class RabbitmqConnection:
    def __init__(self) -> None:
        self.host = "localhost"
        self.port = 5672
        self.username = "guest"
        self.password = "guest"
        self.channel = self.create_channel()

    def start_connection(self):
        pass

    def create_channel(self):
        connection_paramters = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=pika.PlainCredentials(
                username=self.username, password=self.password
            ),
        )

        channel = pika.BlockingConnection(connection_paramters).channel()
        return channel


rabbitmq_connection = RabbitmqConnection()
