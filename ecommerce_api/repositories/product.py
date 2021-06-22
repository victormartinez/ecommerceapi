from typing import List, Dict

from .interfaces import AbstractRepository


class ProductRepository(AbstractRepository):

    def __init__(self, db: List[Dict]):
        self._db = db

    def all(self) -> List[Dict]:
        return self._db

    def filter_by(self, kv: Dict) -> List[Dict]:
        k, v = kv.popitem()
        return [p for p in self.all() if p[k] == v]

    def find_by_ids(self, ids: List[int]) -> List[Dict]:
        return list(filter(lambda x: x["id"] in ids, self.all()))
