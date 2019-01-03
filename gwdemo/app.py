from pecan import make_app

from scmsimagelib import connection


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
