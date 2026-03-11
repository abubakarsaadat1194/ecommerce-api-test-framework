from clients.api_client import APIClient


class ProductService:

    @staticmethod
    def get_all_products():
        return APIClient.get("/products")

    @staticmethod
    def get_product(product_id):
        return APIClient.get(f"/products/{product_id}")

    @staticmethod
    def create_product(payload):
        return APIClient.post("/products", payload)