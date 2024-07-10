import unittest
from unittest.mock import patch
import requests
from test_setup import TestSetup

class TestGetOrderByTrack(TestSetup):

    @patch('requests.get')
    def test_get_order_by_track_successful(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "order": {
                "id": 2,
                "firstName": "Naruto",
                "lastName": "Uzumaki",
                "address": "Kanoha, 142 apt.",
                "metroStation": "1",
                "phone": "+7 800 355 35 35",
                "rentTime": 5,
                "deliveryDate": "2020-06-06T00:00:00.000Z",
                "track": 4,
                "status": 1,
                "color": ["BLACK"],
                "comment": "Saske, come back to Kanoha",
                "cancelled": False,
                "finished": False,
                "inDelivery": False,
                "courierFirstName": "Kaneki",
                "createdAt": "2020-06-08T14:40:28.219Z",
                "updatedAt": "2020-06-08T14:40:28.219Z"
            }
        }

        track_number = 123456
        response = requests.get(f"{self.base_url}/orders/track", params={"t": track_number})

        self.assertEqual(response.status_code, 200, "Expected status code 200 for successful order retrieval")
        self.assertIn("order", response.json(), "Expected order object in response")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(self.format_json(response.json()))

    @patch('requests.get')
    def test_get_order_by_track_missing_track_number(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {"message": "Недостаточно данных для поиска"}

        response = requests.get(f"{self.base_url}/orders/track")

        self.assertEqual(response.status_code, 400, "Expected status code 400 for missing track number")
        self.assertEqual(response.json(), {"message": "Недостаточно данных для поиска"}, "Expected error message for missing track number")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(self.format_json(response.json()))

    @patch('requests.get')
    def test_get_order_by_track_invalid_track_number(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"message": "Заказ не найден"}

        track_number = 999999
        response = requests.get(f"{self.base_url}/orders/track", params={"t": track_number})

        self.assertEqual(response.status_code, 404, "Expected status code 404 for invalid track number")
        self.assertEqual(response.json(), {"message": "Заказ не найден"}, "Expected error message for invalid track number")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(self.format_json(response.json()))

    def format_json(self, json_data, indent=0):
        formatted_output = ""
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                formatted_output += "  " * indent + f"{key}: "
                formatted_output += self.format_json(value, indent + 1) + "\n"
        elif isinstance(json_data, list):
            for item in json_data:
                formatted_output += self.format_json(item, indent + 1)
        else:
            formatted_output += str(json_data)
        return formatted_output

if __name__ == '__main__':
    unittest.main(verbosity=2)

