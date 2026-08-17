import requests
from api.config import BASE_URL

class AuthAPI:

    def verify_credentials(self, email, password):
        payload = {'email': email,
                   'password': password
        }
        response = requests.post(
            f"{BASE_URL}/verifyLogin",
            data=payload
        )
        return response

    def create_user(self, user_data):
        response = requests.post(
            f"{BASE_URL}/createAccount",
            data=user_data
        )
        return response

    def delete_user(self, email, password):
        payload = {'email': email,
                   'password': password}
        response = requests.delete(
            f"{BASE_URL}/deleteAccount",
            data=payload
        )
        return response

    def update_user(self, user_data):
        response = requests.put(
            f"{BASE_URL}/updateAccount",
            data=user_data
        )
        return response

    def get_user_by_email(self, email):
        response = requests.get(
            f"{BASE_URL}/getUserDetailByEmail",
            params={"email": email}
        )
        return response