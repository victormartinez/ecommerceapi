from flask import request
from flask_restful import Resource

from ecommerce_api.constants import ResponseCode
from ecommerce_api.ext.database import db
from ecommerce_api.repositories import ProductRepository
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

        product_repository = ProductRepository(db)
        requested_ids = [d["id"] for d in data_or_exc["products"]]
        invalid_ids = product_repository.get_invalid_ids(requested_ids)
        if invalid_ids:
            return create_response(
                400,
                code=ResponseCode.PRODUCTS_NOT_FOUND.value,
                message="One or more products are invalid.",
                data={"ids": invalid_ids}
            )

        # TODO: implement logic
        return create_response(200)
