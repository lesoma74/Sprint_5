import pytest
import allure
import requests
from data import order_with_color_BLACK
from test_setup import TestSetup


class TestOrderCreationAndRetrieval(TestSetup):

    @allure.title("Получение заказа по его номеру")
    def test_create_and_get_order_by_track_number(self):
        # Создание заказа с определённым цветом (BLACK, например)
        payload = order_with_color_BLACK
        response = requests.post(self.base_url + '/orders', json=payload)

        # Проверка успешности создания заказа
        assert response.status_code == 201, "Expected status code 201 for successful order creation"
        assert "track" in response.json(), "Response should contain 'track' for the order"

        # Получение трек номера созданного заказа
        track_number = response.json()["track"]
        assert track_number, "Expected a valid track number in response"


        # Получение заказа по трек номеру
        response = requests.get(f"{self.base_url}/orders/track?t={track_number}")

        # Проверка успешности получения заказа
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert "order" in response.json(), f"Expected 'order' field in response for order with track number {track_number}"
        order_data = response.json()["order"]
        assert "id" in order_data, "Expected 'id' field in order data"

        # Получение ID заказа
        order_id = order_data["id"]


        # Теперь принимаем заказ по его ID
        courier_id = self.create_courier()
        accept_order_url = f"{self.base_url}/orders/accept/{order_id}?courierId={courier_id}"
        accept_response = requests.put(accept_order_url)

        # Проверка успешности принятия заказа
        assert accept_response.status_code == 200, f"Expected status code 200 for accepting the order, but got {accept_response.status_code}"
        assert accept_response.json().get("ok") is True, "Expected response 'ok' to be True"


if __name__ == '__main__':
    pytest.main()















