#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/1/3 15:44
@desc:
"""
from pecan import expose

from scmsimagelib import sender


class ServiceGatewayController(object):

    @expose(template='json')
    def user_buy(self):
        # mock select the relative chain from db
        chain = 'chain1'
        next_service = 'books'
        message = '{"method": "query_book", "parameter": "user",' \
                  '"content": "user query books"}'
        sender.send_message(message, chain, next_service)

        return 'user query books success \n'

    @expose(template='json')
    def seller_statistics(self):
        # mock select the relative chain from db
        chain = 'chain2'
        next_service = 'books'
        message = '{"method": "query_book", "parameter": "seller",' \
                  '"content": "seller statistics books"}'
        sender.send_message(message, chain, next_service)

        return 'seller statistics books success \n'
