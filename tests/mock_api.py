import responses


def mock_products_api():

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/products",
        json=[{
            "id": 1,
            "title": "Test Product",
            "price": 100.0,
            "description": "Mock product",
            "category": "electronics",
            "image": "https://example.com/img.png"
        }],
        status=200
    )


def mock_users_api():

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/users",
        json=[{
            "id": 1,
            "email": "test@example.com",
            "username": "testuser"
        }],
        status=200
    )


def mock_carts_api():

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/carts",
        json=[{
            "id": 1,
            "userId": 1,
            "date": "2024-01-01"
        }],
        status=200
    )