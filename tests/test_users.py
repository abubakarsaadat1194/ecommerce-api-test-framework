import responses

from services.user_service import UserService
from utils.performance import validate_response_time


@responses.activate
def test_get_all_users():

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/users",
        json=[
            {
                "id": 1,
                "email": "test@example.com",
                "username": "testuser",
                "name": {
                    "firstname": "John",
                    "lastname": "Doe"
                }
            }
        ],
        status=200
    )

    response = UserService.get_all_users()

    validate_response_time(response)

    assert response.status_code == 200

    users = response.json()

    print("Total users:", len(users))

    assert len(users) > 0


@responses.activate
def test_get_single_user():

    responses.add(
        responses.GET,
        "https://fakestoreapi.com/users/1",
        json={
            "id": 1,
            "email": "test@example.com",
            "username": "testuser",
            "name": {
                "firstname": "John",
                "lastname": "Doe"
            }
        },
        status=200
    )

    response = UserService.get_user(1)

    validate_response_time(response)

    assert response.status_code == 200

    user = response.json()

    print(user)

    assert "email" in user