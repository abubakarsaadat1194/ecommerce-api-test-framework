from faker import Faker

fake = Faker()


class UserFactory:

    @staticmethod
    def create():

        return {
            "email": fake.email(),
            "username": fake.user_name(),
            "password": fake.password(),
            "name": {
                "firstname": fake.first_name(),
                "lastname": fake.last_name()
            },
            "address": {
                "city": fake.city(),
                "street": fake.street_name(),
                "number": fake.random_int(min=1, max=100),
                "zipcode": fake.postcode(),
                "geolocation": {
                    "lat": "0",
                    "long": "0"
                }
            },
            "phone": fake.phone_number()
        }