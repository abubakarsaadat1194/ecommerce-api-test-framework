import responses

from services.cart_service import CartService
from utils.performance import validate_response_time
from factories.cart_factory import CartFactory
from tests.mock_api import mock_carts_api

def mock_carts_api():

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/carts",
        json=[
            {
                "id": 1,
                "userId": 1,
                "products": [{"productId": 1, "quantity": 2}]
            }
        ],
        status=200
    )

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/carts/1",
        json={
            "id": 1,
            "userId": 1,
            "products": [{"productId": 1, "quantity": 2}]
        },
        status=200
    )

    responses.add(
        responses.POST,
        "https://fakestoreapi.com/carts",
        json={
            "id": 5,
            "userId": 1,
            "products": [{"productId": 1, "quantity": 2}]
        },
        status=201
    )
@responses.activate
def test_get_all_carts():

    mock_carts_api()

    response = CartService.get_all_carts()

    validate_response_time(response)

    assert response.status_code == 200

    carts = response.json()

    print("Total carts:", len(carts))

    assert len(carts) > 0


@responses.activate
def test_get_single_cart():

    mock_carts_api()

    response = CartService.get_cart(1)

    validate_response_time(response)

    assert response.status_code == 200

    cart = response.json()

    print(cart)

    assert "userId" in cart


@responses.activate
def test_create_cart():

    payload = CartFactory.create()

    mock_carts_api()

    response = CartService.create_cart(payload)

    validate_response_time(response)

    print(response.json())

    assert response.status_code in [200, 201]