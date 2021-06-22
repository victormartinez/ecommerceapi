from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from typing import List

from ..discount.interfaces import AbstractDiscountClient


@dataclass(frozen=False)
class CartProduct:
    id: int
    quantity: int
    unit_amount: int
    total_amount: int
    discount: int
    is_gift: bool


@dataclass(frozen=True)
class Context:
    cart_products: List[CartProduct]
    discount_client: AbstractDiscountClient
    black_friday_date: date


class CartStep(ABC):
    def __init__(self, context: Context):
        self.context = context

    @abstractmethod
    def apply(self) -> List[CartProduct]:
        pass
