#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2018/12/10 14:48
@desc:
"""
from scmsimagelib import connection as conn


def send_message(message, chain, next_service):
    exchange = ''
    routing_key = chain + "_" + next_service

    pika_conn = conn.get_client()
    channel = pika_conn.channel()

    channel.queue_declare(queue=routing_key)

    channel.basic_publish(exchange=exchange,
                          routing_key=routing_key,
                          body=message)
    # not close conn, remain a connection for all

    print("[Send] chain: %s; nextService: %s; message: %s"
          % (chain, next_service, message))
