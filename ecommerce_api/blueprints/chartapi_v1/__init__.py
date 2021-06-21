from flask import Blueprint
from flask_restful import Api

from .resources import ChartResource

bp = Blueprint("chartapi", __name__, url_prefix="/api/v1/chart")
api = Api(bp)


def init_app(app):
    api.add_resource(ChartResource, "/")
    app.register_blueprint(bp)

