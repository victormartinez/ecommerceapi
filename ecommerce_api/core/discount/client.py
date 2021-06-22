from typing import Optional

import grpc

from .interfaces import AbstractDiscountClient
from .discount_pb2 import GetDiscountRequest
from .discount_pb2_grpc import DiscountStub


class DiscountClient(AbstractDiscountClient):

    def __init__(self, host, port, cred=None):
        self.url = f"{host}:{port}"
        self.cred = cred

    def get_discount_percentage(self, product_id: int) -> Optional[float]:
        # TODO: secure channel?
        # TODO: error handling
        try:
            with grpc.insecure_channel(self.url) as channel:
                stub = DiscountStub(channel)
                result = stub.GetDiscount(
                    GetDiscountRequest(productID=product_id)
                )
                return float("{:.2f}".format(result.percentage))
        except grpc.RpcError:
            return None
