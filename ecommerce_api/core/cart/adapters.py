from typing import List, Dict

from .exceptions import ProductsNotFound
from .interfaces import CartProduct


def dict_to_products(requested_products: List[Dict], product_repository) -> List[CartProduct]:
    requested_ids = list(map(lambda x: x["id"], requested_products))
    invalid_ids = product_repository.get_invalid_ids(requested_ids)
    if invalid_ids:
        raise ProductsNotFound(invalid_ids)

    products = product_repository.filter_by_ids(requested_ids)
    products = {p["id"]: p for p in products}

    # TODO: e se não tiver o id no banco?
    return [
        CartProduct(**{
            "id": p["id"],
            "quantity": p["quantity"],
            "unit_amount": products[p["id"]]["amount"],
            "total_amount": products[p["id"]]["amount"] * p["quantity"],
            "discount": 0,
            "is_gift": False,
        })
        for p in requested_products
    ]
