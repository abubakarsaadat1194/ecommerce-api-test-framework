from services.product_service import ProductService
from models.product_model import Product
import pytest
from factories.product_factory import ProductFactory
from services.product_service import ProductService
from models.product_model import Product
from utils.performance import validate_response_time

@pytest.mark.smoke
@pytest.mark.api
def test_get_all_products():

    response = ProductService.get_all_products()

    validate_response_time(response)

    assert response.status_code == 200

    products = response.json()

    for product in products:

        validated_product = Product(**product)

        assert validated_product.price > 0

@pytest.mark.smoke
@pytest.mark.api
def test_get_single_product():

    response = ProductService.get_product(1)

    validate_response_time(response)

    assert response.status_code == 200

@pytest.mark.regression
@pytest.mark.api
def test_create_product():

    payload = ProductFactory.create()

    response = ProductService.create_product(payload)

    validate_response_time(response)

    print(response.json())

    assert response.status_code in [200, 201]