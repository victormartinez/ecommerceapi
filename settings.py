from datetime import datetime

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
    "ecommerce_api.blueprints.cartapi_v1:init_app",
]

API_LIST_KEYS = config("API_LIST_KEYS")
DATABASE_FILENAME = config("DATABASE_FILENAME")
DISCOUNT_SERVICE_HOST = config("DISCOUNT_SERVICE_HOST")
DISCOUNT_SERVICE_PORT = config("DISCOUNT_SERVICE_PORT")
BLACK_FRIDAY_DATE = datetime.strptime(config("BLACK_FRIDAY_DATE"), '%Y-%m-%d').date()
