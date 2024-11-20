from django.urls import reverse
from django.views import generic

from reviews.models import Contact

from ..forms import ContactForm


class ContactView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "reviews/contact_view.html"

    def get_success_url(self) -> str:
        return reverse("contact-sent", kwargs={"pk": self.object.id})


class ContactSent(generic.DetailView):
    model = Contact
    context_object_name = "message"
    template_name = "reviews/contact_sent.html"
