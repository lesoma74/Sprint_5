import pytest
import allure
import requests
from test_setup import TestSetup

@pytest.mark.usefixtures("setup_teardown")
class TestDeleteCourier:

    setup: TestSetup  # Аннотация типа для self.setup

    @allure.title("Удаление существующего курьера")
    def test_delete_courier_successful(self):
        courier_id = self.setup.create_courier()

        response = requests.delete(f"{self.setup.base_url}/courier/{courier_id}")

        assert response.status_code == 200, f"Expected status code 200 for successful courier deletion, got {response.status_code}"
        assert response.json() == {"ok": True}, f"Expected {{'ok': True}} in response for successful deletion, got {response.json()}"

    @allure.title("Удаление курьера с незаполненным id")
    def test_delete_courier_missing_id(self):
        expected_response = {"code": 404, "message": "Not Found."}

        response = requests.delete(f"{self.setup.base_url}/courier/")

        assert response.status_code == 404, f"Expected status code 404 for missing courier id, got {response.status_code}"
        assert response.json() == expected_response, f"Expected {expected_response} in response for missing courier id, got {response.json()}"

    @allure.title("Удаление курьера с несуществующим id")
    def test_delete_courier_invalid_id(self):
        non_existent_courier_id = "999999"  # Assume this ID doesn't exist in the system
        expected_response = {"code": 404, "message": "Курьера с таким id нет."}

        response = requests.delete(f"{self.setup.base_url}/courier/{non_existent_courier_id}")

        assert response.status_code == 404, f"Expected status code 404 for non-existent courier id, got {response.status_code}"
        assert response.json() == expected_response, f"Expected {expected_response} in response for non-existent courier id, got {response.json()}"
