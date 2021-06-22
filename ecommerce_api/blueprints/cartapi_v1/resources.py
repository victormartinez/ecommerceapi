from flask import request
from flask_restful import Resource

import settings
from ecommerce_api.constants import ResponseCode
from ecommerce_api.core.discount import DiscountClient
from ecommerce_api.core.cart import CartPipeline, Context, exceptions
from ecommerce_api.ext.database import db
from ecommerce_api.repositories import ProductRepository
from ecommerce_api.blueprints.presenter import create_response, exc_to_str
from ecommerce_api.blueprints.cartapi_v1.schema import parse_payload


class CartResource(Resource):

    def post(self, *args, **kwargs):
        success, data_or_exc = parse_payload(request)
        if not success:
            return create_response(
                400,
                code=ResponseCode.INVALID_PAYLOAD.value,
                message=exc_to_str(data_or_exc),
            )
        return self._process_cart(data_or_exc["products"])

    def _process_cart(self, products_data):
        try:
            discount_client = DiscountClient(settings.DISCOUNT_SERVICE_HOST, settings.DISCOUNT_SERVICE_PORT)
            context = Context(
                product_repository=ProductRepository(db),
                discount_client=discount_client,
                black_friday_date=settings.BLACK_FRIDAY_DATE,
            )
            data = CartPipeline(products_data, context).process()
            return create_response(200, data=data)
        except exceptions.ProductsNotFound as exc:
            return create_response(
                400,
                code=ResponseCode.PRODUCTS_NOT_FOUND.value,
                message=exc.message,
                data={"ids": exc.product_ids}
            )