from datetime import date

from ecommerce_api.tests.suite import NoDiscountClient, DiscountClient
from ecommerce_api.repositories.product import ProductRepository
from ecommerce_api.core.cart.interfaces import CartProduct, Context
from ecommerce_api.core.cart.pipeline import DiscountStep


def test__discount_step__no_discount(cart_products):
    context = Context(
        product_repository=ProductRepository([]),
        discount_client=NoDiscountClient(),
        black_friday_date=date(1999, 1, 1),
    )
    step = DiscountStep(context, cart_products)
    result_products = step.apply()
    assert result_products == cart_products


def test__discount_step__single_discount(cart_products):
    context = Context(
        product_repository=ProductRepository([]),
        discount_client=DiscountClient([1]),
        black_friday_date=date(1999, 1, 1),
    )
    step = DiscountStep(context, cart_products)
    result_products = step.apply()
    assert result_products == [
        CartProduct(
            **{
                "id": 1,
                "quantity": 1,
                "unit_amount": 15157,
                "total_amount": 15157,
                "discount": 7578,
                "is_gift": False,
            }
        ),
        CartProduct(
            **{
                "id": 2,
                "quantity": 1,
                "unit_amount": 93811,
                "total_amount": 93811,
                "discount": 0,
                "is_gift": False,
            }
        ),
    ]


def test__discount_step__many_discounts(cart_products):
    context = Context(
        product_repository=ProductRepository([]),
        discount_client=DiscountClient([1, 2]),
        black_friday_date=date(1999, 1, 1),
    )
    step = DiscountStep(context, cart_products)
    result_products = step.apply()
    assert result_products == [
        CartProduct(
            **{
                "id": 1,
                "quantity": 1,
                "unit_amount": 15157,
                "total_amount": 15157,
                "discount": 7578,
                "is_gift": False,
            }
        ),
        CartProduct(
            **{
                "id": 2,
                "quantity": 1,
                "unit_amount": 93811,
                "total_amount": 93811,
                "discount": 46906,
                "is_gift": False,
            }
        ),
    ]
