import pytest
import allure
import requests
from data import (
    order_with_color_BLACK,
    order_with_color_GREY,
    order_with_colors_BOTH,
    order_without_color
)
from test_setup import TestSetup

@pytest.mark.usefixtures("setup_teardown")
class TestOrderCreation:

    setup: TestSetup  # Аннотация типа для self.setup

    @pytest.mark.parametrize("name, payload", [
        ("BLACK", order_with_color_BLACK),
        ("GREY", order_with_color_GREY),
        ("BOTH", order_with_colors_BOTH),
        ("NONE", order_without_color)
    ])
    @allure.title("Создание ордера с разными цветами самоката")
    def test_create_order_with_various_colors(self, name, payload):
        response = requests.post(self.setup.base_url + '/orders', json=payload)

        assert response.status_code == 201, f"Expected status code 201 for successful order creation with color {name}"
        assert "track" in response.json(), f"Response should contain 'track' for color {name}"












