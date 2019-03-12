#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/1/3 15:44
@desc:
"""
import time
import uuid

from pecan import expose

from scmsimagelib import sender


class ServiceGatewayController(object):

    @expose(template='json')
    def user_buy(self):
        # mock select the relative chain from db
        chain = 'chain1'
        next_service = 'books'

        id = uuid.uuid1().hex
        # t = time.localtime()
        # TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        # t_start = time.strftime(TIME_FORMAT, t)

        # record time msec
        t_start = int(time.time()*1000)
        message = {"uuid": id, "gw_time": t_start, "chain": chain, "method": "query_book",
                   "parameter": "user", "content": "user query books"}
        sender.send_message(str(message), chain, next_service)

        return 'user query books success \n'

    @expose(template='json')
    def seller_statistics(self):
        # mock select the relative chain from db
        chain = 'chain2'
        next_service = 'books'

        id = uuid.uuid1().hex
        t_start = int(time.time() * 1000)
        message = {"uuid": id, "gw_time": t_start, "chain": chain, "method": "statistics_book",
                   "parameter": "seller", "content": "seller statistics books"}
        sender.send_message(str(message), chain, next_service)

        return 'seller statistics books success \n'
