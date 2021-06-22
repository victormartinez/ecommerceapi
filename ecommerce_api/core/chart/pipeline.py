from typing import List, Dict

from .interfaces import Context, ChartProduct, ChartStep


class DiscountStep(ChartStep):

    def apply(self) -> List[ChartProduct]:
        ids = [p.id for p in self.context.chart_products]
        discounts = {
            idx: self.context.discount_client.get_discount_percentage(product_id=idx)
            for idx in ids
        }
        if not discounts:
            return self.context.chart_products

        products = self.context.chart_products
        for p in products:
            percentage = discounts.get(p.id)
            if p.id in discounts and percentage:
                # TODO: fix percentage
                print("*" * 10)
                print(percentage)
                print("*" * 10)
                p.discount = percentage * p.total_amount

        return products


class BlackFridayStep(ChartStep):

    def apply(self) -> List[ChartProduct]:
        return self.context.chart_products


class GiftProductStep(ChartStep):

    def apply(self) -> List[ChartProduct]:
        return self.context.chart_products


class ChartPipeline:

    def __init__(self, context: Context):
        self.context = context
        self.steps = (
            DiscountStep,
            BlackFridayStep,
            GiftProductStep,
        )

    def process(self) -> Dict:
        products = self.context.chart_products
        for Step in self.steps:
            products = Step(self.context).apply()
        return {"products": products}
