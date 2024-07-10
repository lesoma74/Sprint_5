import unittest
import requests
import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

class TestSetup(unittest.TestCase):
    base_url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    created_courier = None

    def setUp(self):
        self.created_courier = None

    def tearDown(self):
        if self.created_courier:
            # Add code here to delete the courier if needed
            pass

    def register_new_courier_and_return_login_password(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(self.base_url, json=payload)

        if response.status_code == 201:
            self.created_courier = {
                "login": login,
                "password": password,
                "firstName": first_name
            }

        return response

if __name__ == "__main__":
    unittest.main()



