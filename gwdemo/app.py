import pecan
from pecan import make_app

from scmsimagelib import connection
from gwdemo import config


def setup_app(config):

    # model.init_model()
    # mock db

    # here we init the connection to RabbitMQ
    message_server = '192.168.1.220'
    connection.get_client(message_server)

    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        **app_conf
    )


def get_pecan_config():
    filename = config.__file__.replace('.pyc', '.py')   # get the absolute path of the pecan config.py
    return pecan.configuration.conf_from_file(filename)


def setup_app():      # the main functhing, start listening
    # here we init the connection to RabbitMQ
    message_server = '192.168.1.220'
    connection.get_client(message_server)

    config = get_pecan_config()
    app_conf = dict(config.app)
    app = pecan.make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        **app_conf)

    return app