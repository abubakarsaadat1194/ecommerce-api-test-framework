from faker import Faker

fake = Faker()


class ProductFactory:

    @staticmethod
    def create():

        return {
            "title": fake.word(),
            "price": fake.random_int(min=10, max=500),
            "description": fake.sentence(),
            "image": "https://i.pravatar.cc",
            "category": "electronics"
        }