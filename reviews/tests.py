from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def setUp(self) -> None:
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_is_used(self) -> None:
        self.assertTemplateUsed(self.response, "_base.html")
        self.assertTemplateUsed(self.response, "reviews/index.html")

    def test_faux(self):
        self.assertNotContains(self.response, "TEST TEXT")


class ReviewPageTests(TestCase):
    def setUp(self) -> None:
        url = reverse("home")
        self.response = self.client.get(url)

    # def test_url_location_exists(self) -> None:
    #     response = self.client.get("/")
    #     self.assertEqual(response.status_code, 200)

    # def test_url_accessible_by_name(self) -> None:
    #     self.assertEqual(self.response.status_code, 200)

    # def test_correct_template_is_used(self) -> None:
    #     self.assertTemplateUsed(self.response, "_base.html")
    #     self.assertTemplateUsed(self.response, "reviews/index.html")

    # def test_faux(self):
    #     self.assertNotContains(self.response, "TEST TEXT")


class AboutPageTests(TestCase):
    def setUp(self) -> None:
        url = reverse("about")
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get("/despre/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_is_used(self) -> None:
        self.assertTemplateUsed(self.response, "_base.html")
        self.assertTemplateUsed(self.response, "reviews/about_view.html")

    def test_faux(self):
        self.assertNotContains(self.response, "TEST TEXT")


class ContactPageTests(TestCase):
    def setUp(self) -> None:
        url = reverse("contact")
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_is_used(self) -> None:
        self.assertTemplateUsed(self.response, "_base.html")
        self.assertTemplateUsed(self.response, "reviews/contact_view.html")

    def test_faux(self):
        self.assertNotContains(self.response, "TEST TEXT")
