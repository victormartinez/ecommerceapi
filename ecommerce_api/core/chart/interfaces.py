from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from typing import List

from ..discount.interfaces import AbstractDiscountClient


@dataclass(frozen=False)
class ChartProduct:
    id: int
    quantity: int
    unit_amount: int
    total_amount: int
    discount: int
    is_gift: bool


@dataclass(frozen=True)
class Context:
    chart_products: List[ChartProduct]
    discount_client: AbstractDiscountClient
    black_friday_date: date


class ChartStep(ABC):
    def __init__(self, context: Context):
        self.context = context

    @abstractmethod
    def apply(self) -> List[ChartProduct]:
        pass
