#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2018/12/10 14:48
@desc:
"""
import pika

from scmsimagelib import connection as conn


def receive_message(chain, service, callback):
    queue = chain + "_" + service

    channel = conn.get_channel()

    channel.queue_declare(queue=queue)
    channel.basic_consume(callback,
                          queue=queue)

    print(' [*] Waiting for messages. From the queue: ' + queue)
    channel.start_consuming()
