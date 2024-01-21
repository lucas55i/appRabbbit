import pika 

def minha_callback(ch, method, properties, body):
    print(body)

# Conexão
connection_paramters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

# Conexão a fila
channel = pika.BlockingConnection(connection_paramters).channel()
channel.queue_declare(
    queue='app_queue',
    durable=True,
)

# Cria o consumer
channel.basic_consume(
    queue='app_queue',
    auto_ack=True,
    on_message_callback=minha_callback
)

print(f'listen RabbitMQ on Port 5672')
channel.start_consuming()