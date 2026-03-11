from clients.api_client import APIClient


class UserService:

    @staticmethod
    def get_all_users():
        return APIClient.get("/users")

    @staticmethod
    def get_user(user_id):
        return APIClient.get(f"/users/{user_id}")