from rest_framework import status
from rest_framework.test import APITestCase


class AccountTest(APITestCase):
    def test_create_account(self):
        # Arrange
        url = "/api/v1/user"
        data = {
            "email": "usertest@naver.com",
            "name": "test",
            "password": "123",
        }

        # Act
        response = self.client.post(url, data, format="json")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], data["email"])
        self.assertEqual(response.data["name"], data["name"])
