from faker import Faker

fake = Faker()


class CartFactory:

    @staticmethod
    def create():

        return {
            "userId": fake.random_int(min=1, max=5),
            "date": fake.date(),
            "products": [
                {"productId": 1, "quantity": 2},
                {"productId": 2, "quantity": 1}
            ]
        }