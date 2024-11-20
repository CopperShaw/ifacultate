from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .forms import CreateUserForm
from .models.custom_user import CustomUser


class RegisterTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = CustomUser(email="test@mail.com", t_and_c=True)

    def setUp(self) -> None:
        url = reverse("register")
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_is_used(self) -> None:
        self.assertTemplateUsed(self.response, "_base.html")
        self.assertTemplateUsed(self.response, "account/register.html")

    def test_user_model(self) -> None:
        self.assertEqual(str(self.user), "test@mail.com")
        self.assertEqual(self.user.t_and_c, True)

    def test_user_registration_form(self) -> None:
        form_data = {
            "email": self.user.email,
            "password1": "test123!",
            "password2": "test123!",
            "t_and_c": self.user.t_and_c,
        }
        form = CreateUserForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form["email"].value(), "test@mail.com")

    def test_faux(self):
        self.assertNotContains(self.response, "TEST TEXT")


class LoginTests(TestCase):
    def setUp(self) -> None:
        url = reverse("login")
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_is_used(self) -> None:
        self.assertTemplateUsed(self.response, "_base.html")
        self.assertTemplateUsed(self.response, "account/login.html")

    def test_faux(self):
        self.assertNotContains(self.response, "TEST TEXT")


class LogoutTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("logout")
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get("/logout/")
        self.assertEqual(
            response.status_code, 302
        )  # non authenticated user redirects to home page

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 302)

    def test_url_redirects_to_home(self) -> None:
        self.assertRedirects(self.response, reverse("home"))


class DeleteUserTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = CustomUser(email="test@mail.com", t_and_c=True)
        cls.user.save()

    def setUp(self) -> None:
        url = reverse("delete-account", kwargs={"pk": self.user.pk})
        self.response = self.client.get(url)

    # def test_url_location_exists(self) -> None:
    #     response = self.client.get(f"/delete-account/{self.user.pk}/")
    #     self.assertEqual(response.status_code, 302)

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    # def test_user_deletion_works(self) -> None:
    #     # first check that the user exists in the db
    #     pk = self.user.pk
    #     self.assertTrue(self.user)

    #     # delete the user and check that user is gone
    #     self.user.delete()
    #     print(self.user)
    #     self.assertFalse(self.user)


class ProfilePageTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = CustomUser(email="test@mail.com", t_and_c=True)
        cls.user.save()

    def setUp(self) -> None:
        url = reverse("profile", kwargs={"pk": self.user.pk})
        self.response = self.client.get(url)

    def test_url_location_exists(self) -> None:
        response = self.client.get(f"/profile/{self.user.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_is_used(self) -> None:
        # add test for when the user is not authenticated to be redirected to login, implement this in the view, not the template
        self.assertTemplateUsed(self.response, "_base.html")
        self.assertTemplateUsed(self.response, "account/profile.html")

    def test_correct_content_is_displayed(self) -> None:
        self.assertContains(self.response, "Profil")


class MailingStaticPagesTests(SimpleTestCase):
    def test_urls_location_exists(self) -> None:
        response1 = self.client.get("/email-verification-sent/")
        response2 = self.client.get("/email-verification-success/")
        response3 = self.client.get("/email-verification-failed/")
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    def test_urls_accessible_by_name(self) -> None:
        response1 = self.client.get(reverse("email-verification-sent"))
        response2 = self.client.get(reverse("email-verification-success"))
        response3 = self.client.get(reverse("email-verification-failed"))
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    # def test_correct_template_is_used(self) -> None:
    #     # add test for when the user is not authenticated to be redirected to login, implement this in the view, not the template
    #     self.assertTemplateUsed(self.response, "_base.html")
    #     self.assertTemplateUsed(self.response, "account/profile.html")

    # def test_correct_content_is_displayed(self) -> None:
    #     self.assertContains(self.response, "Profil")
