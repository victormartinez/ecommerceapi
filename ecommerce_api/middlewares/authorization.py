import json
from flask import Response

import settings
from ecommerce_api.constants import ResponseCode


class ApikeyAuthorization:

    AUTH_HEADER = "HTTP_X_API_KEY"

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ["REQUEST_URI"] == "/":
            return self.app(environ, start_response)

        if not self._contains_token(environ):
            data = json.dumps(
                {
                    "success": False,
                    "code": ResponseCode.NOT_AUTHORIZED.value,
                    "message": None,
                    "data": None,
                }
            )
            res = Response(data, content_type="application/json", status=401)
            return res(environ, start_response)

        return self.app(environ, start_response)

    def _contains_token(self, environ):
        try:
            if self.AUTH_HEADER not in environ:
                return False

            header_value = environ[self.AUTH_HEADER]
            token = header_value.split("Apikey ")[1]
            available_tokens = [
                t for t in settings.API_LIST_KEYS.split(",") if t
            ]
            return token and token in available_tokens
        except Exception:
            return False
