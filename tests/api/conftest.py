import pytest
from api.clients.auth_api import AuthAPI

@pytest.fixture
def auth_api():
    return AuthAPI()