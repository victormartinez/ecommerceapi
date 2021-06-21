from flask import Blueprint, jsonify
from flask_restful import Api


bp = Blueprint("baseapi", __name__)
api = Api(bp)


def init_app(app):
    @bp.route("/")
    def healthcheck():
        return jsonify({"healthy": True})

    app.register_blueprint(bp)
