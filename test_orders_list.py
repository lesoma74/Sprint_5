import pytest
import allure
import requests
from test_setup import TestSetup


class TestOrdersList(TestSetup):

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = requests.get(f"{self.base_url}/orders")

        assert response.status_code == 200, "Expected status code 200 for successful orders list retrieval"

        try:
            orders = response.json().get("orders", [])
            assert isinstance(orders, list), "'orders' should be a list"
        except Exception as e:
            pytest.fail(f"Error parsing response: {e}")

        # Проверка, что в каждом заказе нет ключа 'courierId' или его значение None
        for order in orders:
            assert "courierId" not in order or order[
                "courierId"] is None, "Expected 'courierId' to be absent or None in each order"


if __name__ == '__main__':
    pytest.main()






