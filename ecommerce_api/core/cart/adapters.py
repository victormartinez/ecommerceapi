from typing import List, Dict

from .exceptions import ProductsNotFound
from .interfaces import CartProduct
from ...repositories.interfaces import AbstractRepository


def dict_to_products(requested_products: List[Dict], product_repository: AbstractRepository) -> List[CartProduct]:
    requested_ids = {p["id"] for p in requested_products}
    products = product_repository.find_by_ids(list(requested_ids))
    if len(requested_ids) != len(products):
        found_ids = {p["id"] for p in products}
        raise ProductsNotFound(requested_ids.difference(found_ids))

    grouped_products = {p["id"]: p for p in products}
    return [
        CartProduct(**{
            "id": p["id"],
            "quantity": p["quantity"],
            "unit_amount": grouped_products[p["id"]]["amount"],
            "total_amount": grouped_products[p["id"]]["amount"] * p["quantity"],
            "discount": 0,
            "is_gift": False,
        })
        for p in requested_products
    ]
