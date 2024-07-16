import pytest
import requests
import random
import string

class TestSetup:
    base_url = 'https://qa-scooter.praktikum-services.ru/api/v1'
    created_courier = None

    def setup_method(self):
        self.created_courier = None

    def teardown_method(self):
        if self.created_courier:
            self.delete_courier(self.created_courier["login"], self.created_courier["password"])

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def register_new_courier_and_return_login_password(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f"{self.base_url}/courier", json=payload)
        print(f"Create courier response status code: {response.status_code}")
        print(f"Create courier response body: {response.json()}")

        if response.status_code == 201:
            login_response = self.login_courier(login, password)
            if login_response.status_code == 200:
                courier_id = login_response.json().get("id")
                if courier_id:
                    self.created_courier = {
                        "login": login,
                        "password": password,
                        "firstName": first_name,
                        "id": courier_id
                    }
                    return response
                else:
                    pytest.fail("Courier created but 'id' not found in response.")
            else:
                pytest.fail(f"Failed to login courier to fetch id: {login_response.status_code}, {login_response.json()}")
        else:
            pytest.fail(f"Failed to create courier: {response.status_code}, {response.json()}")

    def create_courier(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f"{self.base_url}/courier", json=payload)


        if response.status_code == 201:
            # Пытаемся получить id курьера через авторизацию
            login_response = self.login_courier(login, password)
            if login_response.status_code == 200:
                courier_id = login_response.json().get("id")
                if courier_id:
                    self.created_courier = {
                        "login": login,
                        "password": password,
                        "firstName": first_name,
                        "id": courier_id
                    }
                    return courier_id
                else:
                    pytest.fail("Courier login successful but 'id' not found in response.")
            else:
                pytest.fail(
                    f"Failed to login courier to fetch id: {login_response.status_code}, {login_response.json()}")
        else:
            pytest.fail(f"Failed to create courier: {response.status_code}, {response.json()}")

    def login_courier(self, login, password):
        login_url = f"{self.base_url}/courier/login"
        login_response = requests.post(login_url, json={"login": login, "password": password})
        print(f"Login courier response status code: {login_response.status_code}")
        print(f"Login courier response body: {login_response.json()}")
        return login_response

    def delete_courier(self, login, password):
        login_response = self.login_courier(login, password)
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            delete_url = f"{self.base_url}/courier/{courier_id}"
            delete_response = requests.delete(delete_url)
            return delete_response
        return None










