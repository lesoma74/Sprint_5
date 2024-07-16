import pytest
import allure
import requests
from test_setup import TestSetup

@pytest.mark.usefixtures("setup_teardown")
class TestOrdersList:

    setup: TestSetup  # Аннотация типа для self.setup

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = requests.get(f"{self.setup.base_url}/orders")

        assert response.status_code == 200, "Expected status code 200 for successful orders list retrieval"

        orders = response.json().get("orders", [])
        assert isinstance(orders, list), "'orders' should be a list"

        # Проверка, что в каждом заказе нет ключа 'courierId' или его значение None
        for order in orders:
            assert "courierId" not in order or order["courierId"] is None, "Expected 'courierId' to be absent or None in each order"









