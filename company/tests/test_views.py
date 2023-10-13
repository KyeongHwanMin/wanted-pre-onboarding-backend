from rest_framework import status
from rest_framework.test import APITestCase
from company.models import Company


class CompanyTest(APITestCase):
    def test_create_company(self):
        # Arrange
        url = "/api/v1/company"
        data = {"name": "원티드", "nation": "한국", "area": "서울"}

        # Act
        response = self.client.post(url, data, format="json")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_json = response.json()

        company = Company.objects.get()
        self.assertEqual(response_json["id"], company.id)
        self.assertEqual(response_json["name"], company.name)
        self.assertEqual(response_json["nation"], company.nation)
        self.assertEqual(response_json["area"], company.area)
