from django.views import generic


class FAQView(generic.TemplateView):
    template_name = "reviews/faq.html"
