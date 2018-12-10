#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2018/12/10 14:49
@desc:
"""

import threading

import pika
import pika.exceptions as p_ex

_LOCK = threading.Lock()

SERVER = None
PIKA_CONN = None


def init_client(server_ip):
    RABBITMQ_VHOST = "scms"

    global _LOCK
    with _LOCK:
        global PIKA_CONN
        if not PIKA_CONN or not PIKA_CONN.is_open:
            try:
                PIKA_CONN = pika.BlockingConnection(pika.ConnectionParameters(
                    host=server_ip, virtual_host=RABBITMQ_VHOST))
            except p_ex.AMQPConnectionError as e:
                print(e.args)


def get_client(server_ip=SERVER):
     global PIKA_CONN
     if not PIKA_CONN or not PIKA_CONN.is_open:
         init_client(server_ip)

     return PIKA_CONN