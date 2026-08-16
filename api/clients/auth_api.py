import requests
from api.config import BASE_URL

class AuthAPI:

    def verify_credentials(self, email, password):
        payload = {'email': email,
                   'password': password
        }
        response = requests.post(
            f"{BASE_URL}/verifyLogin", data=payload)
        return response

    def create_user(self, user_data):
        response = requests.post(
            f"{BASE_URL}/createAccount", data=user_data
        )
        return response