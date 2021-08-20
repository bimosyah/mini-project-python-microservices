import pika, json

params = pika.URLParameters('amqps://kdpilrrn:8F9XWgk9wvsjSfc4riOTCZ7AvZ5ytqqz@elk.rmq2.cloudamqp.com/kdpilrrn')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',body=json.dumps(body), properties=properties)