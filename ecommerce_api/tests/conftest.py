import pytest

from decouple import config

from ecommerce_api.app import create_app


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
