from services.cart_service import CartService
from utils.performance import validate_response_time
from factories.cart_factory import CartFactory

def test_get_all_carts():

    response = CartService.get_all_carts()

    validate_response_time(response)

    assert response.status_code == 200

    carts = response.json()

    print("Total carts:", len(carts))

    assert len(carts) > 0


def test_get_single_cart():

    response = CartService.get_cart(1)

    validate_response_time(response)

    assert response.status_code == 200

    cart = response.json()

    print(cart)

    assert "userId" in cart

def test_create_cart():

    payload = CartFactory.create()

    response = CartService.create_cart(payload)

    validate_response_time(response)

    print(response.json())

    assert response.status_code in [200, 201]