from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from typing import List, Dict

from ..discount.interfaces import AbstractDiscountClient
from ...repositories.interfaces import AbstractRepository


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
    product_repository: AbstractRepository
    discount_client: AbstractDiscountClient
    black_friday_date: date


class CartStep(ABC):
    def __init__(self, context: Context, products: List[CartProduct]):
        self.context = context
        self.cart_products = products

    @abstractmethod
    def apply(self) -> List[CartProduct]:
        pass
