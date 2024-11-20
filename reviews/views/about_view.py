from django.views import generic


class AboutView(generic.TemplateView):
    template_name = "reviews/about_view.html"
