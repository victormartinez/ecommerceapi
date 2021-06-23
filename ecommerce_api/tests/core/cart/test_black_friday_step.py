from datetime import date

import freezegun

from ecommerce_api.tests.suite import NoDiscountClient
from ecommerce_api.repositories.product import ProductRepository
from ecommerce_api.core.cart.interfaces import Context, CartProduct
from ecommerce_api.core.cart.pipeline import BlackFridayStep


@freezegun.freeze_time("2021-11-26")
def test__blackfriday_step__add_gift(db, cart_products):
    context = Context(
        product_repository=ProductRepository(db),
        discount_client=NoDiscountClient(),
        black_friday_date=date(2021, 11, 26),
    )
    step = BlackFridayStep(context, cart_products)
    result_products = step.apply()
    assert result_products == cart_products + [
        CartProduct(**{
            "id": 6,
            "quantity": 1,
            "unit_amount": 0,
            "total_amount": 0,
            "discount": 0,
            "is_gift": True
        })
    ]


@freezegun.freeze_time("2021-11-25")
def test__blackfriday_step__no_gift(db, cart_products):
    context = Context(
        product_repository=ProductRepository(db),
        discount_client=NoDiscountClient(),
        black_friday_date=date(2021, 11, 26),
    )
    step = BlackFridayStep(context, cart_products)
    result_products = step.apply()
    assert result_products == cart_products
