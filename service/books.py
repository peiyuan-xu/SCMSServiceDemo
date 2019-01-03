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

from scmsimagelib import connection
from scmsimagelib import receiver
from scmsimagelib import sender


global chain
global service
service = "books"


def main(args):
    print("@@@@  Start service a  @@@@@")
    message_server = ""

    global chain
    global service
    chain = None

    try:
        opts, args = getopt.getopt(args, "hs:c:", ["help", "server=", "chain="])
    except getopt.GetoptError:
        print("Error: servicea.py -s <server ip> -c <chain name>")
        print("Or servciea.py --server=<server ip> --chain=<chain name>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("servicea.py -s <server ip> -c <chain name>")
            print("Or servciea.py --server=<server ip> --chain=<chain name>")
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
    receiver.receive_message(chain, service, servicea)


def servicea(ch, method, properties, body):
    print("[Receive] messaage: %s" % body)
    global chain
    global service
    print("[In] chain: %s; service: %s" % (chain, service))
    time.sleep(2)
    ch.basic_ack(delivery_tag=method.delivery_tag)

    # send message to next service
    if "chain1" == chain:
        message = "service a to servie b in chain1"
        next_service = "serviceb"
        sender.send_message(message, chain, next_service)
    elif "chain2" == chain:
        message = "service a to servie c in chain2"
        next_service = "servicec"
        sender.send_message(message, chain, next_service)

    print("[Out] [service a]...\n")


if __name__ == "__main__":
    main(sys.argv[1:])
