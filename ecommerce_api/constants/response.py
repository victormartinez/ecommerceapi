import enum


class ResponseCode(enum.Enum):

    NOT_AUTHORIZED = "not_authorized"
    INVALID_PAYLOAD = "invalid_payload"
    OBJECT_NOT_FOUND = "object_not_found"
    OBJECT_NOT_UPDATED = "object_not_updated"
    OBJECT_NOT_CREATED = "object_not_created"
