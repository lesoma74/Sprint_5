import unittest
from unittest.mock import patch
import requests
from parameterized import parameterized
from data import (
    order_with_color_BLACK,
    order_with_color_GREY,
    order_with_colors_BOTH,
    order_without_color
)
from test_setup import TestSetup

class TestOrderCreation(TestSetup):

    @parameterized.expand([
        ("BLACK", order_with_color_BLACK),
        ("GREY", order_with_color_GREY),
        ("BOTH", order_with_colors_BOTH),
        ("NONE", order_without_color)
    ])
    @patch('requests.post')
    def test_create_order_with_various_colors(self, name, payload, mock_post):
        # Настройка мока для возврата успешного ответа
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"track": 124124}

        response = requests.post(self.base_url + '/orders', json=payload)
        self.assertEqual(response.status_code, 201, f"Expected status code 201 for successful order creation with color {name}")

        # Проверка, что тело ответа содержит track
        self.assertIn("track", response.json(), f"Response should contain 'track' for color {name}")

        # Вывод результатов
        print(f"\nTest case for color {name}:")
        print(f"Response status code: {response.status_code}")
        print("Response body:", response.json())

if __name__ == '__main__':
    # Настройка и запуск тестов с выводом результатов
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOrderCreation)
    result = unittest.TextTestRunner(verbosity=2).run(suite)












