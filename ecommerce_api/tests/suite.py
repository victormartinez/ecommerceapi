from ecommerce_api.core.discount.interfaces import AbstractDiscountClient


class NoDiscountClient(AbstractDiscountClient):

    def get_discount_percentage(self, product_id: int):
        return 0.0


class DiscountClient(AbstractDiscountClient):

    def __init__(self, product_ids):
        self.product_ids = product_ids

    def get_discount_percentage(self, product_id: int):
        return 0.5 if product_id in self.product_ids else 0.0

