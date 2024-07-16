import pytest
import allure
import requests
from data import order_payload
from test_setup import TestSetup

class TestAcceptOrder:
    @classmethod
    def setup_class(cls):
        cls.setup = TestSetup()

    @allure.title("Принятие созданного заказа вновь созданным курьером")
    def test_accept_order_success(self):
        # Создаем курьера для теста
        courier_id = self.setup.create_courier()
        assert courier_id is not None, "Failed to create courier for the test"


        create_order_url = f"{self.setup.base_url}/orders"
        create_order_response = requests.post(create_order_url, json=order_payload)
        assert create_order_response.status_code == 201, f"Failed to create order, status code: {create_order_response.status_code}"
        order_track = create_order_response.json().get("track")
        assert order_track is not None, "Order track is not returned after order creation"


        # Проверяем, существует ли заказ на тестовом сервере
        order_check_url = f"{self.setup.base_url}/orders/track?t={order_track}"
        order_check_response = requests.get(order_check_url)
        assert order_check_response.status_code == 200, f"Order with track {order_track} does not exist"

        order_id = order_check_response.json()['order']['id']

        # Отправляем запрос на принятие заказа на тестовом сервере
        accept_order_url = f"{self.setup.base_url}/orders/accept/{order_id}?courierId={courier_id}"
        response = requests.put(accept_order_url)

        # Проверяем, что запрос вернул статус код 200 и ожидаемый ответ
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        response_body = response.json()
        assert response_body.get("ok") is True, f"Expected response 'ok' to be True, but got {response_body.get('ok')}"
