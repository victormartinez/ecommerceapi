from flask import Blueprint
from flask_restful import Api

from .resources import CartResource

bp = Blueprint("Cartapi", __name__, url_prefix="/api/v1/cart")
api = Api(bp)


def init_app(app):
    api.add_resource(CartResource, "/")
    app.register_blueprint(bp)

