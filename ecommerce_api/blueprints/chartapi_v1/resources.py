from flask import request
from flask_restful import Resource

from ecommerce_api.ext.database import db
from ecommerce_api.constants import ResponseCode
from ecommerce_api.blueprints.presenter import create_response, exc_to_str
from ecommerce_api.blueprints.chartapi_v1.schema import parse_payload


class ChartResource(Resource):

    def post(self, *args, **kwargs):
        success, data_or_exc = parse_payload(request)
        if not success:
            return create_response(
                400,
                code=ResponseCode.INVALID_PAYLOAD.value,
                message=exc_to_str(data_or_exc),
            )

        # TODO: implement logic
        return create_response(200, data=db)