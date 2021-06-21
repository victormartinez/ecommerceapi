from decouple import config

FLASK_APP = config("FLASK_APP")
FLASK_ENV = config("FLASK_ENV")

MIDDLEWARES = [
    "ecommerce_api.middlewares.authorization:ApikeyAuthorization",
]

EXTENSIONS = [
    "ecommerce_api.ext.database:init_app",
]

BLUEPRINTS = [
    "ecommerce_api.blueprints.baseapi_v1:init_app",
    "ecommerce_api.blueprints.chartapi_v1:init_app",
]

API_LIST_KEYS = config("API_LIST_KEYS")
DATABASE_FILENAME = config("DATABASE_FILENAME")
