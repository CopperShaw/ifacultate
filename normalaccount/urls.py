from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (auth_view, delete_account_view,
                    email_verification_failed_view,
                    email_verification_sent_view,
                    email_verification_success_view, email_verification_view,
                    login_view, logout_view, profile_view, register_view)

urlpatterns = [
    path("signup-partial/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("autentificare/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("profile/<uuid:pk>/", profile_view, name="profile"),
    path("delete-account/<uuid:pk>/", delete_account_view, name="delete-account"),
    # password management
    path(
        "reset-password/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset-password-sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "passwod-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # email verification
    path(
        "email-verification/<str:uidb64>/<str:token>/",
        email_verification_view,
        name="email-verification",
    ),
    path(
        "email-verification-sent/",
        email_verification_sent_view,
        name="email-verification-sent",
    ),
    path(
        "email-verification-success/",
        email_verification_success_view,
        name="email-verification-success",
    ),
    path(
        "email-verification-failed/",
        email_verification_failed_view,
        name="email-verification-failed",
    ),
]
