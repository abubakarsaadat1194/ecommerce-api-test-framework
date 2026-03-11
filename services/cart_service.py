from clients.api_client import APIClient


class CartService:

    @staticmethod
    def get_all_carts():
        return APIClient.get("/carts")

    @staticmethod
    def get_cart(cart_id):
        return APIClient.get(f"/carts/{cart_id}")

    @staticmethod
    def create_cart(payload):
        return APIClient.post("/carts", payload)