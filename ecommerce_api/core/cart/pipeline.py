from typing import List, Dict

from .interfaces import Context, CartProduct, CartStep


class DiscountStep(CartStep):

    def apply(self) -> List[CartProduct]:
        ids = [p.id for p in self.context.cart_products]
        discounts = {
            idx: self.context.discount_client.get_discount_percentage(product_id=idx)
            for idx in ids
        }
        if not discounts:
            return self.context.cart_products

        products = self.context.cart_products
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
        return self.context.cart_products


class GiftProductStep(CartStep):

    def apply(self) -> List[CartProduct]:
        return self.context.cart_products


class CartPipeline:

    def __init__(self, context: Context):
        self.context = context
        self.steps = (
            DiscountStep,
            BlackFridayStep,
            GiftProductStep,
        )

    def process(self) -> Dict:
        products = self.context.cart_products
        for Step in self.steps:
            products = Step(self.context).apply()
        return {"products": products}
