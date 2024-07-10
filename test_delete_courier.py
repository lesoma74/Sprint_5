import unittest
from unittest.mock import patch
import requests
from test_setup import TestSetup

class TestDeleteCourier(TestSetup):

    @patch('requests.delete')
    def test_delete_courier_successful(self, mock_delete):
        mock_delete.return_value.status_code = 200
        mock_delete.return_value.json.return_value = {"ok": True}

        courier_id = "3"
        response = requests.delete(f"{self.base_url}/courier/{courier_id}")

        self.assertEqual(response.status_code, 200, "Expected status code 200 for successful courier deletion")
        self.assertEqual(response.json(), {"ok": True}, "Expected {'ok': True} in response for successful deletion")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(response.json())

    @patch('requests.delete')
    def test_delete_courier_missing_id(self, mock_delete):
        mock_delete.return_value.status_code = 400
        mock_delete.return_value.json.return_value = {"message": "Недостаточно данных для удаления курьера"}

        response = requests.delete(f"{self.base_url}/courier/")

        self.assertEqual(response.status_code, 400, "Expected status code 400 for missing courier id")
        self.assertEqual(response.json(), {"message": "Недостаточно данных для удаления курьера"}, "Expected error message for missing courier id")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(response.json())

    @patch('requests.delete')
    def test_delete_courier_invalid_id(self, mock_delete):
        mock_delete.return_value.status_code = 404
        mock_delete.return_value.json.return_value = {"message": "Курьера с таким id нет"}

        courier_id = "999"
        response = requests.delete(f"{self.base_url}/courier/{courier_id}")

        self.assertEqual(response.status_code, 404, "Expected status code 404 for non-existent courier id")
        self.assertEqual(response.json(), {"message": "Курьера с таким id нет"}, "Expected error message for non-existent courier id")
        print(f"HTTP/1.1 {response.status_code} {response.reason}")
        print(response.json())

if __name__ == '__main__':
    unittest.main(verbosity=2)
