from django.test import TestCase
from django.urls import reverse

from universities.models.university import University


class UniversityListTest(TestCase):
    def setUp(self) -> None:
        url = reverse("universitati")
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get("/universitati/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_is_used(self) -> None:
        self.assertTemplateUsed(self.response, "_base.html")
        self.assertTemplateUsed(self.response, "universities/university_list.html")

    def test_faux(self) -> None:
        self.assertNotContains(self.response, "TEST TEXT")


class UniversityDetailTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.university = University(
            name="UNITEST",
            is_private=False,
            description="Oo am comis-o din nou",
            url="https://google.com",
        )
        cls.university.save()

    def setUp(self) -> None:
        url = reverse("universitate", kwargs={"slug": self.university.slug})
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get(f"/universitate/{self.university.slug}")
        self.assertEqual(response.status_code, 200)

    # def test_url_accessible_by_name(self) -> None:
    #     self.assertEqual(self.response.status_code, 200)

    # def test_correct_template_is_used(self) -> None:
    #     self.assertTemplateUsed(self.response, "_base.html")
    #     self.assertTemplateUsed(self.response, "universities/university_list.html")

    # def test_faux(self) -> None:
    #     self.assertNotContains(self.response, "TEST TEXT")
