from utils.test_data import USER_DATA, UPDATE_USER_DATA

from api.clients.auth_api import AuthAPI


def test_auth_api():
    auth_api = AuthAPI()

    response = auth_api.verify_credentials(
        "glenn010@gmail.com",
        "glenn010")

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User exists!"

    print(response.text)
    print(data)


def test_invalid_credentials():
    auth_api = AuthAPI()

    response = auth_api.verify_credentials(
        "maryclaire@gmail.com",
        "glenn00")

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User not found!"
    assert data["responseCode"] == 404

    print(response.text)
    print(data)

def test_create_user():
    auth_api = AuthAPI()

    response = auth_api.create_user(USER_DATA)

    data = response.json()

    print("n\------------")
    print(f"Response Code: {data['responseCode']}")
    print(f"Status: {data['message']}")
    print("----------------")

    assert response.status_code == 200
    assert data["responseCode"] == 201

def test_delete_account():
    auth_api = AuthAPI()

    response = auth_api.delete_user(
        "glenn_reedz@gmail.com",
        "black123412"
    )
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"

def test_update_user_account():
    auth_api = AuthAPI()

    response = auth_api.update_user(UPDATE_USER_DATA)

    print(response.status_code)
    print(response.text)

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"

def test_get_user_by_email():
    auth_api = AuthAPI()

    response = auth_api.get_user_by_email("glenn_black@gmail.com")
    print(response.status_code)
    print(response.text)

def test_full_crud_cycle():
    auth_api = AuthAPI()

    create_user = auth_api.create_user(USER_DATA)
    data = create_user.json()
    assert create_user.status_code == 200
    assert data["responseCode"] == 201
    assert data["message"] == "User created!"

    get_user = auth_api.get_user_by_email("glenn_reedz@gmail.com")
    get_data = get_user.json()
    assert get_user.status_code == 200
    assert get_data["responseCode"] == 200

    update_user = auth_api.update_user(UPDATE_USER_DATA)
    update_data = update_user.json()

    assert update_user.status_code == 200
    assert update_data["responseCode"] == 200

    get_updated_user = auth_api.get_user_by_email("glenn_reedz@gmail.com")
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











