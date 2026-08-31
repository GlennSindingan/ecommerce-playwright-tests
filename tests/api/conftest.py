import pytest
from api.clients.auth_api import AuthAPI
from utils.test_data import USER_DATA

@pytest.fixture
def auth_api():
    return AuthAPI()

@pytest.fixture
def created_user(auth_api):
    response = auth_api.create_user(USER_DATA)

    yield response

    auth_api.delete_user(
        USER_DATA['email'],
        USER_DATA['password']
    )