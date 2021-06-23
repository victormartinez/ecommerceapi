import pytest

from decouple import config

from ecommerce_api.app import create_app
from ecommerce_api.core.cart.interfaces import CartProduct


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["SERVER_NAME"] = "localhost:5000"
    app.config["TESTING"] = True
    return app


@pytest.fixture(scope="module")
def apikey():
    keys = config("API_LIST_KEYS")
    return keys.split(",")[0]


@pytest.fixture
def cart_products():
    return [
        CartProduct(**{
            "id": 1,
            "quantity": 1,
            "unit_amount": 15157,
            "total_amount": 15157,
            "discount": 0,
            "is_gift": False
        }),
        CartProduct(**{
            "id": 2,
            "quantity": 1,
            "unit_amount": 93811,
            "total_amount": 93811,
            "discount": 0,
            "is_gift": False
        })
    ]


@pytest.fixture(scope="module")
def db():
    return [
        {
            "id": 1,
            "title": "Ergonomic Wooden Pants",
            "description": "Deleniti beatae porro.",
            "amount": 15157,
            "is_gift": False
        },
        {
            "id": 2,
            "title": "Ergonomic Cotton Keyboard",
            "description": "Iste est ratione excepturi repellendus adipisci qui.",
            "amount": 93811,
            "is_gift": False
        },
        {
            "id": 3,
            "title": "Gorgeous Cotton Chips",
            "description": "Nulla rerum tempore rem.",
            "amount": 60356,
            "is_gift": False
        },
        {
            "id": 4,
            "title": "Fantastic Frozen Chair",
            "description": "Et neque debitis omnis quam enim cupiditate.",
            "amount": 56230,
            "is_gift": False
        },
        {
            "id": 5,
            "title": "Incredible Concrete Soap",
            "description": "Dolorum nobis temporibus aut dolorem quod qui corrupti.",
            "amount": 42647,
            "is_gift": False
        },
        {
            "id": 6,
            "title": "Handcrafted Steel Towels",
            "description": "Nam ea sed animi neque qui non quis iste.",
            "amount": 900,
            "is_gift": True
        }
    ]