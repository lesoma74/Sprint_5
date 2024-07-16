import pytest
import allure
import requests
from test_setup import TestSetup

@pytest.mark.usefixtures("setup_teardown")
class TestCourierLogin:

    setup: TestSetup  # Аннотация типа для self.setup

    @allure.title("Авторизация нового курьера")
    def test_successful_login(self):
        # Создаем нового курьера и получаем его данные для логина
        response = self.setup.register_new_courier_and_return_login_password()
        assert response.status_code == 201, f"Expected status code 201 for successful creation, got {response.status_code}"

        # Подготавливаем данные для запроса логина
        login_payload = {
            "login": self.setup.created_courier["login"],
            "password": self.setup.created_courier["password"]
        }

        # Отправляем запрос на сервер для авторизации курьера
        response = requests.post(f"{self.setup.base_url}/courier/login", json=login_payload)

        # Проверяем ожидаемый статус код и наличие данных в ответе
        assert response.status_code == 200, f"Expected status code 200 for successful login, got {response.status_code}"
        assert "id" in response.json(), "Response should contain 'id'"

    @allure.title("Авторизация курьера с одним логином")
    def test_login_missing_login(self):
        self.setup.register_new_courier_and_return_login_password()

        login_payload = {
            "password": self.setup.created_courier["password"]
        }
        response = requests.post(f"{self.setup.base_url}/courier/login", json=login_payload)

        assert response.status_code == 400, "Expected status code 400 when login is missing"
        assert "message" in response.json(), "Response should contain 'message'"
        assert response.json()["message"] == "Недостаточно данных для входа", "Expected error message when login is missing"

    @allure.title("Авторизация курьера с неверным логином")
    def test_login_invalid_credentials(self):
        self.setup.register_new_courier_and_return_login_password()

        login_payload = {
            "login": self.setup.created_courier["login"],
            "password": "wrongpassword"
        }
        response = requests.post(f"{self.setup.base_url}/courier/login", json=login_payload)

        assert response.status_code == 404, "Expected status code 404 for invalid credentials"
        assert "message" in response.json(), "Response should contain 'message'"
        assert response.json()["message"] == "Учетная запись не найдена", "Expected error message for invalid credentials"

    @allure.title("Авторизация курьера под несуществующим пользователем")
    def test_login_nonexistent_user(self):
        self.setup.register_new_courier_and_return_login_password()

        login_payload = {
            "login": "nonexistent_user",
            "password": "randompassword"
        }
        response = requests.post(f"{self.setup.base_url}/courier/login", json=login_payload)

        assert response.status_code == 404, "Expected status code 404 for nonexistent user"
        assert "message" in response.json(), "Response should contain 'message'"
        assert response.json()["message"] == "Учетная запись не найдена", "Expected error message for nonexistent user"







