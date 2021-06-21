from decouple import config

FLASK_APP = config("FLASK_APP")
FLASK_ENV = config("FLASK_ENV")

MIDDLEWARES = [
    "ecommerce_api.middlewares.authorization:ApikeyAuthorization",
]

EXTENSIONS = [
]

BLUEPRINTS = [
    "ecommerce_api.blueprints.baseapi_v1:init_app",
]

API_LIST_KEYS = config("API_LIST_KEYS")
