from services.user_service import UserService
from utils.performance import validate_response_time


def test_get_all_users():

    response = UserService.get_all_users()

    validate_response_time(response)

    assert response.status_code == 200

    users = response.json()

    print("Total users:", len(users))

    assert len(users) > 0


def test_get_single_user():

    response = UserService.get_user(1)

    validate_response_time(response)

    assert response.status_code == 200

    user = response.json()

    print(user)

    assert "email" in user