from datetime import date
from typing import List, Dict

from .adapters import dict_to_products
from .interfaces import Context, CartProduct, CartStep


class DiscountStep(CartStep):
    def apply(self) -> List[CartProduct]:
        ids = [p.id for p in self.cart_products]
        discounts = {
            idx: self.context.discount_client.get_discount_percentage(idx)
            for idx in ids
        }
        if not discounts:
            return self.cart_products

        products = self.cart_products
        for p in products:
            percentage = discounts.get(p.id)
            if p.id in discounts and percentage:
                p.discount = round(percentage * p.total_amount)

        return products


class BlackFridayStep(CartStep):
    def apply(self) -> List[CartProduct]:
        if not self._is_black_friday():
            return self.cart_products

        gift_products = self.context.product_repository.filter_by(
            {"is_gift": True}
        )
        if not gift_products:
            return self.cart_products

        gift = CartProduct(
            **{
                "id": gift_products[0]["id"],
                "quantity": 1,
                "unit_amount": 0,
                "total_amount": 0,
                "discount": 0,
                "is_gift": True,
            }
        )
        return self.cart_products + [gift]

    def _is_black_friday(self):
        bf_day, bf_month = (
            self.context.black_friday_date.day,
            self.context.black_friday_date.month,
        )
        today_day, today_month = date.today().day, date.today().month
        return (bf_day == today_day) and (bf_month == today_month)


class GiftProductStep(CartStep):

    GIFT_LIMIT = 1

    def apply(self) -> List[CartProduct]:
        gift_count = sum([p.quantity if p.is_gift else 0 for p in self.cart_products])
        if gift_count <= self.GIFT_LIMIT:
            return self.cart_products

        not_gift = self._get_not_gift_products()
        gift_products = self._get_gift_products()
        return not_gift + gift_products

    def _get_not_gift_products(self):
        return [p for p in self.cart_products if not p.is_gift]

    def _get_gift_products(self):
        gift_products = []
        for p in self.cart_products:
            if p.is_gift:
                p.quantity = 1
                gift_products.append(p)
        return gift_products[: self.GIFT_LIMIT]


class CartPipeline:
    def __init__(
        self,
        cart_products: List[Dict],
        context: Context,
    ):
        """ "
        raises:
            ProductsNotFound
        """
        self.cart_products = dict_to_products(
            cart_products, context.product_repository
        )
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

        total_amount = sum([p.total_amount for p in products])
        total_discount = sum([p.discount for p in products])
        total_amount_with_discount = total_amount - total_discount
        return {
            "total_amount": total_amount,
            "total_amount_with_discount": total_amount_with_discount,
            "total_discount": total_discount,
            "products": [p.to_dict() for p in products],
        }
