from datetime import date

import pytest

from ecommerce_api.tests.suite import DiscountClient
from ecommerce_api.repositories.product import ProductRepository
from ecommerce_api.core.cart.interfaces import CartProduct, Context
from ecommerce_api.core.cart.pipeline import GiftProductStep


@pytest.fixture
def context():
    return Context(
        product_repository=ProductRepository([]),
        discount_client=DiscountClient([]),
        black_friday_date=date(1999, 1, 1),
    )


def test__no_gifts__nothing_changes(context, cart_products):
    step = GiftProductStep(context, cart_products)
    result_products = step.apply()
    assert result_products == cart_products


def test__one_gift__nothing_changes(context, cart_products):
    products = cart_products + [
        CartProduct(**{
            "id": 6,
            "quantity": 1,
            "unit_amount": 0,
            "total_amount": 0,
            "discount": 0,
            "is_gift": True
        })
    ]
    step = GiftProductStep(context, products)
    result_products = step.apply()
    assert result_products == products


def test__one_gift_two_qty__reduces(context, cart_products):
    products = cart_products + [
        CartProduct(**{
            "id": 6,
            "quantity": 2,
            "unit_amount": 0,
            "total_amount": 0,
            "discount": 0,
            "is_gift": True
        })
    ]
    step = GiftProductStep(context, products)
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


def test__two_gifts__reduces(context, cart_products):
    products = cart_products + [
        CartProduct(**{
            "id": 6,
            "quantity": 2,
            "unit_amount": 0,
            "total_amount": 0,
            "discount": 0,
            "is_gift": True
        }),
        CartProduct(**{
            "id": 7,
            "quantity": 1,
            "unit_amount": 0,
            "total_amount": 0,
            "discount": 0,
            "is_gift": True
        })
    ]
    step = GiftProductStep(context, products)
    result_products = step.apply()
    assert result_products == cart_products + [
        CartProduct(**{
            "id": 6,
            "quantity": 1,
            "unit_amount": 0,
            "total_amount": 0,
            "discount": 0,
            "is_gift": True
        }),
    ]