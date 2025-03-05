#!/usr/bin/env python
# coding=utf-8
import pika

# Устанавливаем соединение с RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Объявляем очередь, если она еще не существует
channel.queue_declare(queue='hello')

# Функция обратного вызова, которая будет вызываться при получении сообщения
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Подписываемся на очередь и указываем функцию обратного вызова
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# Начинаем бесконечный цикл ожидания сообщений
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()