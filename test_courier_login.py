import unittest
from unittest.mock import patch
import requests
from test_setup import TestSetup, generate_random_string

class TestCourierLogin(TestSetup):

    @patch('requests.post')
    def test_successful_login(self, mock_post):
        # Setup the mock response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"id": 12345}

        login_payload = {
            "login": "ninja",
            "password": "1234"
        }
        response = requests.post(f"{self.base_url}/courier/login", json=login_payload)

        self.assertEqual(response.status_code, 200, f"Expected status code 200 for successful login, got {response.status_code}")
        self.assertIn("id", response.json(), "Response should contain 'id'")
        self.assertEqual(response.json()["id"], 12345, "Expected courier ID 12345")

        # Test result output
        print(f"HTTP Status Code: {response.status_code}")
        print(f"JSON Response: {response.json()}")

    @patch('requests.post')
    def test_login_missing_login(self, mock_post):
        # Setup the mock response
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"message": "Недостаточно данных для входа"}

        login_payload = {
            "password": "1234"
        }
        response = requests.post(f"{self.base_url}/courier/login", json=login_payload)

        self.assertEqual(response.status_code, 400, "Expected status code 400 when login is missing")
        self.assertIn("message", response.json(), "Response should contain 'message'")
        self.assertEqual(response.json()["message"], "Недостаточно данных для входа",
                         "Expected error message 'Недостаточно данных для входа' when login is missing")

        # Test result output
        print(f"HTTP Status Code: {response.status_code}")
        print(f"JSON Response: {response.json()}")

    @patch('requests.post')
    def test_login_missing_password(self, mock_post):
        # Setup the mock response
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"message": "Недостаточно данных для входа"}

        login_payload = {
            "login": "ninja"
        }
        response = requests.post(f"{self.base_url}/courier/login", json=login_payload)

        self.assertEqual(response.status_code, 400, "Expected status code 400 when password is missing")
        self.assertIn("message", response.json(), "Response should contain 'message'")
        self.assertEqual(response.json()["message"], "Недостаточно данных для входа",
                         "Expected error message 'Недостаточно данных для входа' when password is missing")

        # Test result output
        print(f"HTTP Status Code: {response.status_code}")
        print(f"JSON Response: {response.json()}")

    @patch('requests.post')
    def test_login_invalid_credentials(self, mock_post):
        # Setup the mock response
        mock_post.return_value.status_code = 404
        mock_post.return_value.json.return_value = {"message": "Учетная запись не найдена"}

        login_payload = {
            "login": "ninja",
            "password": "wrongpassword"
        }
        response = requests.post(f"{self.base_url}/courier/login", json=login_payload)

        self.assertEqual(response.status_code, 404, "Expected status code 404 for invalid credentials")
        self.assertIn("message", response.json(), "Response should contain 'message'")
        self.assertEqual(response.json()["message"], "Учетная запись не найдена",
                         "Expected error message 'Учетная запись не найдена' for invalid credentials")

        # Test result output
        print(f"HTTP Status Code: {response.status_code}")
        print(f"JSON Response: {response.json()}")

    @patch('requests.post')
    def test_login_nonexistent_user(self, mock_post):
        # Setup the mock response
        mock_post.return_value.status_code = 404
        mock_post.return_value.json.return_value = {"message": "Учетная запись не найдена"}

        login_payload = {
            "login": "nonexistent_user",
            "password": "randompassword"
        }
        response = requests.post(f"{self.base_url}/courier/login", json=login_payload)

        self.assertEqual(response.status_code, 404, "Expected status code 404 for nonexistent user")
        self.assertIn("message", response.json(), "Response should contain 'message'")
        self.assertEqual(response.json()["message"], "Учетная запись не найдена",
                         "Expected error message 'Учетная запись не найдена' for nonexistent user")

        # Test result output
        print(f"HTTP Status Code: {response.status_code}")
        print(f"JSON Response: {response.json()}")

if __name__ == "__main__":
    unittest.main()
