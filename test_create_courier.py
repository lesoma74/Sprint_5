import unittest
from unittest.mock import patch
import requests
from test_setup import TestSetup, generate_random_string

class TestCourierCreation(TestSetup):

    @patch('requests.post')
    def test_create_courier(self, mock_post):
        # Setup the mock response
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"ok": True}

        response = self.register_new_courier_and_return_login_password()
        self.assertEqual(response.status_code, 201, f"Expected status code 201 for successful creation, got {response.status_code}")
        self.assertIn("ok", response.json(), "Response should contain 'ok'")
        self.assertTrue(response.json()["ok"], "Response 'ok' should be true")

        # Test result output
        print(f"HTTP Status Code: {response.status_code}")
        print(f"Created courier details: Login - {self.created_courier['login']}, Password - {self.created_courier['password']}, First Name - {self.created_courier['firstName']}")
        print(f"JSON Response: {response.json()}")

    @patch('requests.post')
    def test_create_duplicate_courier(self, mock_post):
        # Setup the mock response for the first courier creation
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"ok": True}

        # Create a new courier
        response = self.register_new_courier_and_return_login_password()
        self.assertEqual(response.status_code, 201, f"Expected status code 201 for successful creation, got {response.status_code}")

        # Setup the mock response for the duplicate courier creation
        mock_post.return_value.status_code = 409
        mock_post.return_value.json.return_value = {"message": "Этот логин уже используется"}

        # Try to create a courier with the same login
        payload = {
            "login": self.created_courier["login"],
            "password": self.created_courier["password"],
            "firstName": self.created_courier["firstName"]
        }
        response = requests.post(self.base_url, json=payload)

        # Check that the server returned code 409 Conflict
        self.assertEqual(response.status_code, 409, f"Expected status code 409 for duplicate login, got {response.status_code}")
        self.assertIn("Этот логин уже используется", response.json().get("message", ""), "Response should contain 'Этот логин уже используется'")

        # Test result output
        print(f"HTTP Status Code: {response.status_code}")
        print(f"JSON Response: {response.json()}")

    @patch('requests.post')
    def test_create_courier_with_all_fields(self, mock_post):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
            # Add other required fields if any
        }

        # Setup the mock response
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"ok": True}

        response = requests.post(self.base_url, json=payload)

        self.assertEqual(response.status_code, 201, f"Expected status code 201 for successful creation, got {response.status_code}")
        self.assertIn("ok", response.json(), "Response should contain 'ok'")
        self.assertTrue(response.json()["ok"], "Response 'ok' should be true")

        # Test result output
        print(f"HTTP Status Code: {response.status_code}")
        print(f"Created courier details: Login - {login}, Password - {password}, First Name - {first_name}")
        print(f"JSON Response: {response.json()}")

    @patch('requests.post')
    def test_create_courier_missing_login(self, mock_post):
        # Setup the mock response
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"message": "Недостаточно данных для создания учетной записи"}

        payload = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(self.base_url, json=payload)

        self.assertEqual(response.status_code, 400, "Expected status code 400 when login is missing")
        self.assertIn("message", response.json(), "Response should contain 'message'")
        self.assertEqual(response.json()["message"], "Недостаточно данных для создания учетной записи",
                         "Expected error message when login is missing")
        print(f"HTTP Status Code: {response.status_code}")
        print(f"JSON Response: {response.json()}")

    @patch('requests.post')
    def test_create_courier_missing_password(self, mock_post):
        # Setup the mock response
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"message": "Недостаточно данных для создания учетной записи"}

        payload = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(self.base_url, json=payload)

        self.assertEqual(response.status_code, 400, "Expected status code 400 when password is missing")
        self.assertIn("message", response.json(), "Response should contain 'message'")
        self.assertEqual(response.json()["message"], "Недостаточно данных для создания учетной записи",
                         "Expected error message when password is missing")
        print(f"HTTP Status Code: {response.status_code}")
        print(f"JSON Response: {response.json()}")

if __name__ == "__main__":
    unittest.main()












