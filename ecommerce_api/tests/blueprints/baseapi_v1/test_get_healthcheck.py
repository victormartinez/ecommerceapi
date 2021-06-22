def test__healthcheck__success(app):
    with app.test_client() as client:
        response = client.get("/")
        assert response == 200
        assert response.json == {"healthy": True}
