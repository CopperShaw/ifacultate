from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from normalaccount.models import CustomUser


class RequiredBooleanField(forms.BooleanField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.required = True

    def validate(self, value):
        super().validate(value)
        if not value:
            raise forms.ValidationError(self.error_messages["required"])


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _("Contul și parola nu se potrivesc."),
        "inactive": _("Contul este inactiv."),
    }

    class Meta:
        model = CustomUser
        fields = ["username", "password"]

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Adresă de Email", "class": "auth-form-field"}
        ),
        label="",
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Parolă", "class": "auth-form-field"},
        ),
        label="",
    )


class CreateUserForm(UserCreationForm):
    error_messages = {
        "password_mismatch": _("Cele două parole introduse sunt diferite."),
    }

    t_and_c = RequiredBooleanField(
        label=mark_safe(
            "<span class='t_and_c'>Am citit, înțeles și sunt de acord cu <a href='/termeni-conditii/'>Termenii și condițiile</a>, <a href='/prelucrare-date/'>Politica de confidențialitate</a></span>"
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Adresă de Email",
                "class": "auth-form-field",
                "autofocus": False,
            }
        ),
        error_messages={
            "required": "Vă rugăm să introduceți o adresă de email.",
            "invalid": "Adresă de email invalidă.",
        },
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Parolă", "class": "auth-form-field"},
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirmă parola", "class": "auth-form-field"},
        ),
    )

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2", "t_and_c"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.pop("autofocus", None)
