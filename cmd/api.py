#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/15 14:38
@desc:
"""
from wsgiref import simple_server
from gwdemo import app


def main():
    application = app.setup_app()

    srv = simple_server.make_server('', 8081, application)
    print('Server on port 8081, listening...')

    srv.serve_forever()


if __name__ == '__main__':
    main()
