from rest_framework import status
from company.models import Company
from rest_framework.test import APITestCase
from recruitment_notice.models import RecruitmentNotice


class RecruitmentNoticeTest(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(name="원티드랩", nation="한국", area="서울")

        self.recruitment_notice = RecruitmentNotice.objects.create(
            company=self.company,
            position="주니어 개발자",
            compensation=50000000,
            content="원티드랩에서 백엔드 주니어 개발자를 채용합니다.",
            skill="파이썬",
        )

    def test_create_recruitmentnotice(self):
        # Arrange
        url = "/api/v1/recruitment-notice"
        data = {
            "회사_id": self.company.id,
            "채용포지션": "주니어 개발자",
            "채용보상금": 5000000,
            "채용내용": "원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은...",
            "사용기술": "파이썬",
        }

        # Act
        response = self.client.post(url, data, format="json")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_json = response.json()

        recruitment_notice = RecruitmentNotice.objects.latest("created_at")

        self.assertEqual(response_json["회사_id"], recruitment_notice.company_id)
        self.assertEqual(response_json["채용포지션"], recruitment_notice.position)
        self.assertEqual(response_json["채용보상금"], recruitment_notice.compensation)
        self.assertEqual(response_json["채용내용"], recruitment_notice.content)
        self.assertEqual(response_json["사용기술"], recruitment_notice.skill)

    def test_update_recruitmentnotice(self):
        # Arrange
        url = f"/api/v1/recruitment-notice/{self.recruitment_notice.id}"
        data = {
            "채용포지션": "백엔드 개발자",
            "채용보상금": 200000,
            "채용내용": "원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은",
            "사용기술": "Django",
        }

        # Act
        response = self.client.patch(url, data, format="json")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()

        recruitment_notice = RecruitmentNotice.objects.get()
        self.assertEqual(response_json["채용포지션"], recruitment_notice.position)
        self.assertEqual(response_json["채용보상금"], recruitment_notice.compensation)
        self.assertEqual(response_json["채용내용"], recruitment_notice.content)
        self.assertEqual(response_json["사용기술"], recruitment_notice.skill)

    def test_delete_recruitmentnotice(self):
        # Arrange
        url = f"/api/v1/recruitment-notice/{self.recruitment_notice.id}"

        # Act
        response = self.client.delete(url)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(RecruitmentNotice.DoesNotExist):
            RecruitmentNotice.objects.get(id=self.recruitment_notice.id)

    def test_list_recruitmentnotice(self):
        # Arrange
        url = "/api/v1/recruitment-notice"

        # Act
        response = self.client.get(url, format="json")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for recruitment_notice in response.data:
            self.assertIn("채용공고_id", recruitment_notice)
            self.assertIn("회사명", recruitment_notice)
            self.assertIn("국가", recruitment_notice)
            self.assertIn("지역", recruitment_notice)
            self.assertIn("채용포지션", recruitment_notice)
            self.assertIn("채용보상금", recruitment_notice)
            self.assertIn("사용기술", recruitment_notice)
