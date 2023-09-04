"""
    Beth Harvey
    September 4, 2023
    This program sends a message to a queue on the RabbitMQ server.

"""

# add imports at the beginning of the file
import pika

# define message to send
MESSAGE = 'Now I can send all the messages!'

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to declare a queue
ch.queue_declare(queue="hello")

# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=f'{MESSAGE}')

# print a message to the console for the user
print(f" [x] Sent {MESSAGE}")

# close the connection to the server
conn.close()
