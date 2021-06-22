from typing import List, Dict


class ProductRepository:

    def __init__(self, db: List[Dict]):
        self.db = db

    def filter_by_id(self, ids: List[int]) -> List[Dict]:
        return list(filter(lambda x: x["id"] in ids, self.db))

    def get_invalid_ids(self, ids: List[int]) -> List[int]:
        product_ids = list(map(lambda x: x["id"], self.db))
        return [i for i in ids if i not in product_ids]