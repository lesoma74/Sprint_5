# test_orders_list.py

import unittest
from unittest.mock import patch
import requests
from data import orders_list_response, orders_list_not_found_response
from test_setup import TestSetup

class TestOrdersList(TestSetup):

    @patch('requests.get')
    def test_get_orders_list(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = orders_list_response

        response = requests.get(self.base_url + '/orders')
        self.assertEqual(response.status_code, 200, "Expected status code 200 for successful orders list retrieval")
        self.assertEqual(response.json(), orders_list_response, "Expected orders list response")
        print(f"HTTP/1.1 {response.status_code} {response.json()}")

    @patch('requests.get')
    def test_get_orders_list_with_nonexistent_courier(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = orders_list_not_found_response

        response = requests.get(self.base_url + '/orders?courierId=999')
        self.assertEqual(response.status_code, 404, "Expected status code 404 for nonexistent courierId")
        self.assertEqual(response.json(), orders_list_not_found_response, "Expected courier not found response")
        print(f"HTTP/1.1 {response.status_code} {response.json()}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
