from typing import Optional

import grpc

from .interfaces import AbstractDiscountClient
from .discount_pb2 import GetDiscountRequest
from .discount_pb2_grpc import DiscountStub


class DiscountClient(AbstractDiscountClient):
    def __init__(self, host, port):
        self.url = f"{host}:{port}"

    def get_discount_percentage(self, product_id: int) -> Optional[float]:
        try:
            with grpc.insecure_channel(self.url) as channel:
                stub = DiscountStub(channel)
                result = stub.GetDiscount(
                    GetDiscountRequest(productID=product_id)
                )
                return float("{:.2f}".format(result.percentage))
        except grpc.RpcError:
            return None
