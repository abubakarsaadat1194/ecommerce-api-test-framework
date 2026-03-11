import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def product_payload():

    payload = {
        "title": fake.word(),
        "price": fake.random_int(min=10, max=100),
        "description": fake.sentence(),
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }

    return payload

@pytest.fixture
def cart_payload():

    payload = {
        "userId": 1,
        "date": "2024-03-01",
        "products": [
            {"productId": 1, "quantity": 2},
            {"productId": 2, "quantity": 1}
        ]
    }

    return payload