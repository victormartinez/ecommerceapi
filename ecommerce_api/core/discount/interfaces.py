from abc import ABC, abstractmethod

from typing import Optional


class AbstractDiscountClient(ABC):
    @abstractmethod
    def get_discount_percentage(self, product_id: int) -> Optional[float]:
        pass
