from django.views import generic


class DateView(generic.TemplateView):
    template_name = "reviews/date.html"
