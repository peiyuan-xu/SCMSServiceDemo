#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2018/12/10 10:43
@desc:
"""

import sys
import getopt

def main(args):
    message_server = ""
    chain = ""
    service_name = "servicea"

    try:
        opts, args = getopt.getopt(args, "hs:c", ["help", "server=", "chain="])
    except getopt.GetoptError:
        print("Error: ")
