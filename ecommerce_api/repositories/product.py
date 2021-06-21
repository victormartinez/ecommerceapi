from typing import List, Dict

from ecommerce_api.ext.database import db


class ProductRepository:

    @staticmethod
    def filter_by_id(ids: List[int]) -> List[Dict]:
        return list(filter(lambda x: x["id"] in ids, db))

    @staticmethod
    def get_invalid_ids(ids: List[int]) -> List[int]:
        product_ids = list(map(lambda x: x["id"], db))
        return [i for i in ids if i not in product_ids]