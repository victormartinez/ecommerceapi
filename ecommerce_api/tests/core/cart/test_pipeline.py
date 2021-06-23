from datetime import date

import freezegun

from ecommerce_api.tests.suite import DiscountClient
from ecommerce_api.repositories.product import ProductRepository
from ecommerce_api.core.cart.interfaces import Context
from ecommerce_api.core.cart.pipeline import CartPipeline


@freezegun.freeze_time("2021-11-26")
def test__full__pipeline(db):
    context = Context(
        product_repository=ProductRepository(db),
        discount_client=DiscountClient([1, 2]),
        black_friday_date=date(2021, 11, 26),
    )
    products = [{"id": 1, "quantity": 2}, {"id": 2, "quantity": 1}]
    output = CartPipeline(products, context).process()
    assert output == {
        "total_amount": 124125,
        "total_amount_with_discount": 62062,
        "total_discount": 62063,
        "products": [
            {
                "id": 1,
                "quantity": 2,
                "unit_amount": 15157,
                "total_amount": 30314,
                "discount": 15157,
                "is_gift": False
            },
            {
                "id": 2,
                "quantity": 1,
                "unit_amount": 93811,
                "total_amount": 93811,
                "discount": 46906,
                "is_gift": False
            },
            {
                "id": 6,
                "quantity": 1,
                "unit_amount": 0,
                "total_amount": 0,
                "discount": 0,
                "is_gift": True
            }
        ],
    }