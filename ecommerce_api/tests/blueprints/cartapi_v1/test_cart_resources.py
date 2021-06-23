from unittest import mock


def _post_request(client, data, apikey):
    path = "/api/v1/cart/"
    return client.post(
        path, json=data, headers={"X-API-KEY": f"Apikey {apikey}"}
    )


def test__post_cart__unauthorized(app):
    with app.test_client() as client:
        response = _post_request(client, {}, "")
        assert response == 401


def test__post_cart__invalid_payload(app, apikey):
    with app.test_client() as client:
        response = _post_request(client, {}, apikey)
        assert response == 400
        assert response.json == {
            "code": "invalid_payload",
            "data": None,
            "message": "{'products': ['Missing data for required field.']}",
            "success": False,
        }


@mock.patch(
    (
        "ecommerce_api.blueprints.cartapi_v1.resources"
        ".DiscountClient.get_discount_percentage"
    )
)
def test__post_cart__success(discount_mock, app, apikey):
    discount_mock.return_value = 0.0

    with app.test_client() as client:
        data = {
            "products": [{"id": 1, "quantity": 2}, {"id": 2, "quantity": 2}]
        }
        response = _post_request(client, data, apikey)
        assert response == 200
        assert response.json == {
            "message": None,
            "success": True,
            "code": None,
            "data": {
                "total_amount": 217936,
                "total_amount_with_discount": 217936,
                "total_discount": 0,
                "products": [
                    {
                        "discount": 0,
                        "id": 1,
                        "is_gift": False,
                        "quantity": 2,
                        "total_amount": 30314,
                        "unit_amount": 15157,
                    },
                    {
                        "discount": 0,
                        "id": 2,
                        "is_gift": False,
                        "quantity": 2,
                        "total_amount": 187622,
                        "unit_amount": 93811,
                    },
                ],
            },
        }


@mock.patch(
    (
        "ecommerce_api.blueprints.cartapi_v1.resources"
        ".DiscountClient.get_discount_percentage"
    )
)
def test__post_cart__success_with_discount(discount_mock, app, apikey):
    discount_mock.return_value = 0.5
    with app.test_client() as client:
        data = {
            "products": [{"id": 1, "quantity": 2}, {"id": 2, "quantity": 2}]
        }
        response = _post_request(client, data, apikey)
        assert response == 200
        assert response.json == {
            "message": None,
            "success": True,
            "code": None,
            "data": {
                "total_amount": 217936,
                "total_amount_with_discount": 108968,
                "total_discount": 108968,
                "products": [
                    {
                        "discount": 15157,
                        "id": 1,
                        "is_gift": False,
                        "quantity": 2,
                        "total_amount": 30314,
                        "unit_amount": 15157,
                    },
                    {
                        "discount": 93811,
                        "id": 2,
                        "is_gift": False,
                        "quantity": 2,
                        "total_amount": 187622,
                        "unit_amount": 93811,
                    },
                ],
            },
        }
