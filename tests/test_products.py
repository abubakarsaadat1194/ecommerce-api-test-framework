import responses
import pytest

from services.product_service import ProductService
from models.product_model import Product
from factories.product_factory import ProductFactory
from utils.performance import validate_response_time


@pytest.mark.smoke
@pytest.mark.api
@responses.activate
def test_get_all_products():

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/products",
        json=[
            {
                "id": 1,
                "title": "Mock Product",
                "price": 120.0,
                "description": "Test product",
                "category": "electronics",
                "image": "https://example.com/product.png"
            }
        ],
        status=200
    )

    response = ProductService.get_all_products()

    validate_response_time(response)

    assert response.status_code == 200

    products = response.json()

    for product in products:

        validated_product = Product(**product)

        assert validated_product.price > 0


@pytest.mark.smoke
@pytest.mark.api
@responses.activate
def test_get_single_product():

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/products/1",
        json={
            "id": 1,
            "title": "Mock Product",
            "price": 120.0,
            "description": "Test product",
            "category": "electronics",
            "image": "https://example.com/product.png"
        },
        status=200
    )

    response = ProductService.get_product(1)

    validate_response_time(response)

    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.api
@responses.activate
def test_create_product():

    payload = ProductFactory.create()

    responses.add(
        responses.POST,
        "https://fakestoreapi.com/products",
        json={
            "id": 11,
            **payload
        },
        status=201
    )

    response = ProductService.create_product(payload)

    validate_response_time(response)

    print(response.json())

    assert response.status_code in [200, 201]