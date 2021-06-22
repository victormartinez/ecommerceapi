from typing import List, Dict

from .exceptions import ProductsNotFound
from .interfaces import CartProduct
from ...repositories.interfaces import AbstractRepository


def dict_to_products(requested_products: List[Dict], product_repository: AbstractRepository) -> List[CartProduct]:
    requested_ids = [p["id"] for p in requested_products]
    all_ids = [p["id"] for p in product_repository.all()]
    invalid_ids = [i for i in requested_ids if i not in all_ids]
    if invalid_ids:
        raise ProductsNotFound(invalid_ids)

    products = product_repository.find_by_ids(requested_ids)
    grouped_products = {p["id"]: p for p in products}

    # TODO: e se não tiver o id no banco?
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
