import unittest
from unittest.mock import patch
import requests
from test_setup import TestSetup

class TestAcceptOrder(TestSetup):

    @patch('requests.put')
    def test_accept_order_successful(self, mock_put):
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = {"ok": True}

        courier_id = 213
        order_id = 1

        response = requests.put(f"{self.base_url}/orders/accept/{order_id}", params={"courierId": courier_id})
        self.assertEqual(response.status_code, 200, "Expected status code 200 for successful order acceptance")
        self.assertEqual(response.json(), {"ok": True}, "Expected successful response")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(self.format_json(response.json()))

    @patch('requests.put')
    def test_accept_order_missing_courierId(self, mock_put):
        mock_put.return_value.status_code = 400
        mock_put.return_value.json.return_value = {"message": "Недостаточно данных для поиска"}

        order_id = 1

        response = requests.put(f"{self.base_url}/orders/accept/{order_id}")
        self.assertEqual(response.status_code, 400, "Expected status code 400 for missing courierId")
        self.assertEqual(response.json(), {"message": "Недостаточно данных для поиска"}, "Expected error message for missing courierId")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(self.format_json(response.json()))

    @patch('requests.put')
    def test_accept_order_invalid_courierId(self, mock_put):
        mock_put.return_value.status_code = 404
        mock_put.return_value.json.return_value = {"message": "Курьера с таким id не существует"}

        courier_id = 999
        order_id = 1

        response = requests.put(f"{self.base_url}/orders/accept/{order_id}", params={"courierId": courier_id})
        self.assertEqual(response.status_code, 404, "Expected status code 404 for invalid courierId")
        self.assertEqual(response.json(), {"message": "Курьера с таким id не существует"}, "Expected error message for invalid courierId")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(self.format_json(response.json()))

    @patch('requests.put')
    def test_accept_order_missing_orderId(self, mock_put):
        mock_put.return_value.status_code = 400
        mock_put.return_value.json.return_value = {"message": "Недостаточно данных для поиска"}

        courier_id = 213

        response = requests.put(f"{self.base_url}/orders/accept/", params={"courierId": courier_id})
        self.assertEqual(response.status_code, 400, "Expected status code 400 for missing orderId")
        self.assertEqual(response.json(), {"message": "Недостаточно данных для поиска"}, "Expected error message for missing orderId")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(self.format_json(response.json()))

    @patch('requests.put')
    def test_accept_order_invalid_orderId(self, mock_put):
        mock_put.return_value.status_code = 404
        mock_put.return_value.json.return_value = {"message": "Заказа с таким id не существует"}

        courier_id = 213
        order_id = 999

        response = requests.put(f"{self.base_url}/orders/accept/{order_id}", params={"courierId": courier_id})
        self.assertEqual(response.status_code, 404, "Expected status code 404 for invalid orderId")
        self.assertEqual(response.json(), {"message": "Заказа с таким id не существует"}, "Expected error message for invalid orderId")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(self.format_json(response.json()))

    def format_json(self, json_data, indent=0):
        formatted_output = ""
        for key, value in json_data.items():
            if isinstance(value, list):
                formatted_output += "  " * indent + f"{key}:\n"
                for item in value:
                    formatted_output += self.format_json(item, indent + 1)
            elif isinstance(value, dict):
                formatted_output += "  " * indent + f"{key}:\n"
                formatted_output += self.format_json(value, indent + 1)
            else:
                formatted_output += "  " * indent + f"{key}: {value}\n"
        return formatted_output

if __name__ == '__main__':
    unittest.main(verbosity=2)



