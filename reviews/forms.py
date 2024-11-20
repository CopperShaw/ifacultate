from django import forms

from faculties.models import Faculty
from universities.models import University

from .models import Contact, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "university",
            "faculty",
            "grad_promo",
            "user_type",
            "pro",
            "against",
            "advice",
            "rating",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Titlu (min. 10 caractere)"}
            ),
            "grad_promo": forms.TextInput(
                attrs={"placeholder": "Promoția (ex. 2020-2024)"}
            ),
            "user_type": forms.Select(attrs={"placeholder": "Select user type"}),
            "pro": forms.Textarea(
                attrs={
                    "placeholder": "Enumeră câteva aspecte pozitive (min. 50 caractere)",
                    "class": "textarea-field",
                }
            ),
            "against": forms.Textarea(
                attrs={
                    "placeholder": "Enumeră câteva aspecte negative (min. 50 caractere)",
                    "class": "textarea-field",
                }
            ),
            "advice": forms.Textarea(
                attrs={
                    "placeholder": "Sfaturi (min. 50 caractere)",
                    "class": "textarea-field",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        slug_university = kwargs.pop("slug_university", None)
        slug_faculty = kwargs.pop("slug_faculty", None)

        super().__init__(*args, **kwargs)

        # Override error messages for specific fields
        self.fields["title"].error_messages = {
            "required": "Vă rugăm să introduceți un titlu.",
            "min_length": "Titlul trebuie să aibă cel puțin %(limit_value)d caractere.",
        }
        self.fields["grad_promo"].error_messages = {
            "required": "Vă rugăm să introduceți promoția.",
        }
        self.fields["pro"].error_messages = {
            "required": "Vă rugăm să enumerați câteva aspecte pozitive.",
            "min_length": "Aspectele pozitive trebuie să aibă cel puțin %(limit_value)d caractere.",
        }
        self.fields["against"].error_messages = {
            "required": "Vă rugăm să enumerați câteva aspecte negative.",
            "min_length": "Aspectele negative trebuie să aibă cel puțin %(limit_value)d caractere.",
        }
        self.fields["advice"].error_messages = {
            "required": "Vă rugăm să oferiți câteva sfaturi.",
            "min_length": "Sfaturile trebuie să aibă cel puțin %(limit_value)d caractere.",
        }
        self.fields["rating"].error_messages = {
            "required": "Vă rugăm să oferiți o evaluare generală.",
            "invalid": "Evaluarea trebuie să fie un număr valid.",
        }

        university = None
        faculty = None

        if slug_university:
            try:
                university = University.objects.get(slug=slug_university)
            except University.DoesNotExist:
                pass  # Handle missing university (optional)

        if slug_faculty:
            if university:
                try:
                    faculty = Faculty.objects.get(
                        slug=slug_faculty, university=university
                    )
                except Faculty.DoesNotExist:
                    pass  # Handle missing faculty (optional)

        if faculty:
            self.fields["university"].initial = faculty.university
            self.fields["faculty"].initial = faculty
        elif university:
            self.fields["university"].initial = university
            self.fields["faculty"].queryset = Faculty.objects.filter(
                university=university
            )
        else:
            self.fields["university"].queryset = University.objects.all()
            self.fields["university"].widget.attrs["placeholder"] = "Alege universitate"
            self.fields["faculty"].widget.attrs["placeholder"] = "Alege facultate"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["title", "email", "text"]

    # title email text
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Titlu", "class": "contact-form-field"}
        ),
        error_messages={"required": "Vă rugăm să introduceți un titlu."},
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Adresă de Email", "class": "contact-form-field"}
        ),
        error_messages={
            "required": "Vă rugăm să introduceți o adresă de email.",
            "invalid": "Adresă de email invalidă.",
        },
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Mesajul tău",
                "class": "contact-form-field",
                "cols": 0,
                "rows": 5,
            }
        ),
        error_messages={"required": "Vă rugăm să introduceți un mesaj"},
    )
