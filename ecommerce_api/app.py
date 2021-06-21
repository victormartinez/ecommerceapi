from flask import Flask

from ecommerce_api.ext import configuration


def create_app(*args, **config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    configuration.load_extensions(app)
    configuration.load_blueprints(app)
    configuration.load_middlewares(app)
    return app
