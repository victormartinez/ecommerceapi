from typing import List


class ProductsNotFound(Exception):

    def __init__(self, product_ids: List[int]):
        self.product_ids = product_ids
        self.message = "One or more products are invalid."
        super().__init__(self.message)
