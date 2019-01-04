#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2018/12/10 10:43
@desc:
"""

import sys
import time
import getopt
import json

from scmsimagelib import connection
from scmsimagelib import receiver
from scmsimagelib import sender


global chain
global service
service = "books"


def main(args):
    print("@@@@  Start service books  @@@@@")
    message_server = ""

    global chain
    global service
    chain = None

    try:
        opts, args = getopt.getopt(args, "hs:c:", ["help", "server=", "chain="])
    except getopt.GetoptError:
        print("Error: books.py -s <server ip> -c <chain name>")
        print("Or books.py --server=<server ip> --chain=<chain name>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("books.py -s <server ip> -c <chain name>")
            print("Or books.py --server=<server ip> --chain=<chain name>")
            sys.exit()
        elif opt in ("-s", "--server"):
            message_server = arg
            # print("server : %s" % message_server)
        elif opt in ("-c", "--chain"):
            chain = arg
            # print("chain : %s" % chain)

    # check the args
    if not message_server or not chain:
        print("Error: server ip and chain name can't be none")
        sys.exit(2)

    # init pika connection and start receiving message
    connection.SERVER = message_server
    connection.get_client(message_server)
    receiver.receive_message(chain, service, books)


def books(ch, method, properties, body):
    global chain
    global service
    print("[In] chain: %s; service: %s \n" % (chain, service))

    # mock real time-consuming
    time.sleep(2)

    body_str = body.decode()
    body_dict = json.loads(body_str)
    method_name = body_dict.get('method')
    parameter = body_dict.get('parameter')
    content = body_dict.get('content')

    # send message to next service
    if 'query_book' == method_name:
        query_book()
    elif 'statistics_book' == method_name:
        statistics_book()

    ch.basic_ack(delivery_tag=method.delivery_tag)

    print("[Out] chain: %s; service: %s \n" % (chain, service))


def query_book():
    message = '{"method": "query_review", "parameter": "user",' \
                  '"content": "user query reviews"}'
    next_service = "reviews"
    sender.send_message(message, chain, next_service)
    print("send message to review \n")


def statistics_book():
    message = '{"method": "query_score", "parameter": "seller",' \
                  '"content": "seller query score"}'
    next_service = "score"
    sender.send_message(message, chain, next_service)
    print("send message to score \n")


if __name__ == "__main__":
    main(sys.argv[1:])
