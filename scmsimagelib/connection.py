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
CHANNEL = None


def init_client(server_ip):
    RABBITMQ_VHOST = "scms"
    RABBITMQ_USER = "scms"
    RABBITMQ_PWD = "scms"

    global _LOCK
    with _LOCK:
        global PIKA_CONN
        if not PIKA_CONN or not PIKA_CONN.is_open:
            try:
                credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PWD)
                PIKA_CONN = pika.BlockingConnection(pika.ConnectionParameters(
                    host=server_ip, virtual_host=RABBITMQ_VHOST, credentials=credentials))
            except p_ex.AMQPConnectionError as e:
                print(e.args)


def get_client(server_ip=SERVER):
    global PIKA_CONN
    if not PIKA_CONN or not PIKA_CONN.is_open:
        init_client(server_ip)

    return PIKA_CONN


def get_channel():
    global PIKA_CONN
    global CHANNEL
    global SERVER

    if not PIKA_CONN or not PIKA_CONN.is_open:
        init_client(SERVER)

    if not CHANNEL or not CHANNEL.is_open:
        try:
            CHANNEL = PIKA_CONN.channel()
        except pika.exceptions.ConnectionClosed:
            init_client(SERVER)
            CHANNEL = PIKA_CONN.channel()

    return CHANNEL
