from typing import Iterable, Optional


class ProductsNotFound(Exception):
    def __init__(self, product_ids: Optional[Iterable[int]] = None):
        self.product_ids = product_ids or []
        self.message = "One or more products are invalid."
        super().__init__(self.message)
