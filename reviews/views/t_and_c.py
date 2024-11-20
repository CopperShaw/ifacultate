from django.views import generic


class TermsView(generic.TemplateView):
    template_name = "reviews/t_and_c.html"
