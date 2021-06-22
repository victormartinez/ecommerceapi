import enum


class ResponseCode(enum.Enum):

    NOT_AUTHORIZED = "not_authorized"
    INVALID_PAYLOAD = "invalid_payload"
    PRODUCTS_NOT_FOUND = "products_not_found"
    CART_PROCESSING_ERROR = "cart_processing_error"
