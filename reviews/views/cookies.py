from django.views import generic


class CookiesView(generic.TemplateView):
    template_name = "reviews/cookies.html"
