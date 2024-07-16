import allure
import requests
import pytest
from test_setup import TestSetup

@pytest.mark.usefixtures("setup_teardown")
class TestCourierCreation:

    @allure.title("Создание нового курьера")
    def test_create_courier(self):
        response = self.setup.register_new_courier_and_return_login_password()
        assert response.status_code == 201, f"Expected status code 201 for successful creation, got {response.status_code}"
        assert "ok" in response.json(), "Response should contain 'ok'"

    @allure.title("Создание дубликата курьера")
    def test_create_duplicate_courier(self):
        response = self.setup.register_new_courier_and_return_login_password()
        assert response.status_code == 201, f"Expected status code 201 for successful creation, got {response.status_code}"

        # Try to create a courier with the same login
        payload = {
            "login": self.setup.created_courier["login"],
            "password": self.setup.created_courier["password"],
            "firstName": self.setup.created_courier["firstName"]
        }
        response = requests.post(f"{self.setup.base_url}/courier", json=payload)

        # Check that the server returned code 409 Conflict
        assert response.status_code == 409, f"Expected status code 409 for duplicate login, got {response.status_code}"
        assert "Этот логин уже используется" in response.json().get("message", "")

    @allure.title("Создание курьера с заполнением обязательных полей")
    def test_create_courier_with_all_fields(self):
        login = self.setup.generate_random_string(10)
        password = self.setup.generate_random_string(10)
        first_name = self.setup.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
            # Add other required fields if any
        }

        response = requests.post(f"{self.setup.base_url}/courier", json=payload)

        assert response.status_code == 201, f"Expected status code 201 for successful creation, got {response.status_code}"
        assert "ok" in response.json(), "Response should contain 'ok'"

    @allure.title("Создание курьера с незаполненным полем логин")
    def test_create_courier_missing_login(self):
        payload = {
            "password": self.setup.generate_random_string(10),
            "firstName": self.setup.generate_random_string(10)
        }
        response = requests.post(f"{self.setup.base_url}/courier", json=payload)

        assert response.status_code == 400, "Expected status code 400 when login is missing"
        assert "message" in response.json(), "Response should contain 'message'"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Создание курьера с незаполненным полем пароль")
    def test_create_courier_missing_password(self):
        payload = {
            "login": self.setup.generate_random_string(10),
            "firstName": self.setup.generate_random_string(10)
        }
        response = requests.post(f"{self.setup.base_url}/courier", json=payload)

        assert response.status_code == 400, "Expected status code 400 when password is missing"
        assert "message" in response.json(), "Response should contain 'message'"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
