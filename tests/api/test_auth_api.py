from utils.test_data import USER_DATA, UPDATE_USER_DATA, BASE_USER_DATA, NO_USER_DATA, ANOTHER_BASE_USER_DATA
import pytest


def test_auth_api(auth_api):

    response = auth_api.verify_credentials(
        "glenn010@gmail.com",
        "glenn010")

    assert response.status_code == 200
    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"

def test_create_user(auth_api):

    response = auth_api.create_user(USER_DATA)

    data = response.json()

    print("n\------------")
    print(f"Response Code: {data['responseCode']}")
    print(f"Status: {data['message']}")
    print("----------------")

    assert response.status_code == 200
    assert data["responseCode"] == 201

def test_update_user_account(auth_api):

    response = auth_api.update_user(UPDATE_USER_DATA)

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"

def test_get_user_by_email(auth_api):

    response = auth_api.get_user_by_email("beautiful_sadness@gmail.com")
    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 200
    assert data["user"]["email"] == "beautiful_sadness@gmail.com"

def test_delete_account(auth_api):

    response = auth_api.delete_user(
        "mono_no_aware@gmail.com",
        "611611"
    )
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"

    # FULL CYCLE #

def test_full_crud_cycle(auth_api):

    create_user = auth_api.create_user(USER_DATA)
    data = create_user.json()
    assert create_user.status_code == 200
    assert data["responseCode"] == 201
    assert data["message"] == "User created!"

    get_user = auth_api.get_user_by_email(USER_DATA["email"])
    get_data = get_user.json()
    assert get_user.status_code == 200
    assert get_data["responseCode"] == 200

    update_user = auth_api.update_user(UPDATE_USER_DATA)
    update_data = update_user.json()

    assert update_user.status_code == 200
    assert update_data["responseCode"] == 200

    get_updated_user = auth_api.get_user_by_email(USER_DATA["email"])
    get_data = get_updated_user.json()
    assert get_updated_user.status_code == 200
    assert get_data["responseCode"] == 200
    assert get_data["user"]["first_name"] == "Black"
    assert get_data["user"]["last_name"] == "Hole"

    delete_user = auth_api.delete_user(
        "glenn_reedz@gmail.com",
        "black123412"
    )
    delete_data = delete_user.json()
    assert delete_user.status_code == 200
    assert delete_data["responseCode"] == 200
    assert delete_data["message"] == "Account deleted!"

    get_deleted_user = auth_api.get_user_by_email("glenn_reedz@gmail.com")
    deleted_data = get_deleted_user.json()
    assert deleted_data["message"] == "Account not found with this email, try another email!"
    assert deleted_data["responseCode"] == 404
    print("CRUD flow is working successfully!")


# NEGATIVE TESTING

@pytest.mark.parametrize(
    "email, password",
    [
        ("maryclaire@gmail.com", "invalid123"),
        ("kalapastangan@gmail.com", "wrong123"),
        ("withoutu@gmail.com", "password123")
    ]
)
def test_invalid_credentials(auth_api, email, password):
    response = auth_api.verify_credentials(email, password)

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User not found!"
    assert data["responseCode"] == 404


@pytest.mark.parametrize(
    "user_data",
    [
        BASE_USER_DATA,
        ANOTHER_BASE_USER_DATA
    ]
)
def test_create_existing_user(auth_api, user_data):

    response = auth_api.create_user(user_data)
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Email already exists!"
    assert data["responseCode"] == 400

def test_delete_non_existing_user(auth_api):

    response = auth_api.delete_user(
        "davidsoon@gmail.com",
        "passwooor322"
    )
    assert response.status_code == 200
    data = response.json()

    assert data["responseCode"] == 404
    assert data["message"] == "Account not found!"

def test_get_non_existing_user(auth_api):

    response = auth_api.get_user_by_email("davidsoon@gmail.com")
    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 404
    assert data["message"] == "Account not found with this email, try another email!"

def test_update_non_existing_user(auth_api):

    response = auth_api.update_user(NO_USER_DATA)
    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 404
    assert data["message"] == "Account not found!"

    # TODO: Continue full crud cycle | make it independent and reliable











