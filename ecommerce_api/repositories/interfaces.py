from abc import ABC, abstractmethod
from typing import List, Dict


class AbstractRepository(ABC):
    @abstractmethod
    def all(self) -> List[Dict]:
        pass

    @abstractmethod
    def filter_by(self, kv: Dict):
        pass

    @abstractmethod
    def find_by_ids(self, ids: List[int]) -> List[Dict]:
        pass
