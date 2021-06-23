import pytest

from ecommerce_api.core.cart.exceptions import ProductsNotFound
from ecommerce_api.core.cart.interfaces import CartProduct
from ecommerce_api.core.cart.adapters import dict_to_products
from ecommerce_api.repositories.product import ProductRepository


def test__adapter__success(db):
    requested_products = [{"id": 2, "quantity": 2}]
    products = dict_to_products(requested_products, ProductRepository(db))
    assert len(products) == 1
    assert products[0] == CartProduct(
        **{
            "id": 2,
            "quantity": 2,
            "unit_amount": 93811,
            "total_amount": 187622,
            "discount": 0,
            "is_gift": False,
        }
    )


def test__adapter__product_not_found(db):
    with pytest.raises(ProductsNotFound):
        requested_products = [{"id": 9999, "quantity": 1}]
        dict_to_products(requested_products, ProductRepository(db))


def test__adapter__database_empty():
    with pytest.raises(ProductsNotFound):
        requested_products = [{"id": 1, "quantity": 1}]
        dict_to_products(requested_products, ProductRepository([]))
