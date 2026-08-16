from http.client import responses

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

    user_data = {
        "name": "Glenn",
        "email": "glenn_test_987654@gmail.com",
        "password": "12345",
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "7",
        "birth_year": "2000",
        "firstname": "Glenn",
        "lastname": "Test",
        "company": "Test Company",
        "address1": "Test Address",
        "address2": "",
        "country": "India",
        "zipcode": "12345",
        "state": "Test State",
        "city": "Test City",
        "mobile_number": "1234567890"
    }
    response = auth_api.create_user(user_data)

    print("STATUS:", response.status_code)
    print("BODY:", response.text)
    print("URL:", response.url)

def test_delete_account():
    auth_api = AuthAPI()

    response = auth_api.delete_user(
        "glenn_test_987654@gmail.com",
        "12345"
    )
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    wendie = response.json()

    assert wendie["responseCode"] == 200
    assert wendie["message"] == "Account deleted!"



