from typing import List, Dict

from .adapters import dict_to_products
from .interfaces import Context, CartProduct, CartStep


class DiscountStep(CartStep):

    def apply(self) -> List[CartProduct]:
        ids = [p.id for p in self.cart_products]
        discounts = {
            idx: self.context.discount_client.get_discount_percentage(product_id=idx)
            for idx in ids
        }
        if not discounts:
            return self.cart_products

        products = self.cart_products
        for p in products:
            percentage = discounts.get(p.id)
            if p.id in discounts and percentage:
                # TODO: fix percentage
                print("*" * 10)
                print(percentage)
                print("*" * 10)
                p.discount = percentage * p.total_amount

        return products


class BlackFridayStep(CartStep):

    def apply(self) -> List[CartProduct]:
        return self.cart_products


class GiftProductStep(CartStep):

    def apply(self) -> List[CartProduct]:
        return self.cart_products


class CartPipeline:

    def __init__(
        self,
        cart_products: List[Dict],
        context: Context,
    ):
        """"
        raises:
            ProductsNotFound
        """
        self.cart_products = dict_to_products(cart_products, context.product_repository)
        self.context = context
        self.steps = (
            DiscountStep,
            BlackFridayStep,
            GiftProductStep,
        )

    def process(self) -> Dict:
        products = self.cart_products
        for Step in self.steps:
            products = Step(self.context, products).apply()
        return {"products": products}
