from .auth_views import (auth_view, delete_account_view,
                         email_verification_failed_view,
                         email_verification_sent_view,
                         email_verification_success_view,
                         email_verification_view, login_view, logout_view,
                         profile_view, register_view)

__all__ = [
    register_view,
    login_view,
    logout_view,
    profile_view,
    delete_account_view,
    email_verification_view,
    email_verification_success_view,
    email_verification_failed_view,
    email_verification_sent_view,
    auth_view,
]
