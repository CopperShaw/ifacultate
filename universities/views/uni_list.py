from typing import Any

from django.views.generic import ListView
from django.db.models import Count, Q

from faculties.models import County
from universities.models import University

from reviews.models import Review


class UniversityListView(ListView):
    model = University
    template_name = "university_list.html"  # default
    context_object_name = "universities"  # Optional, default is 'object_list'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UniversityListView, self).get_context_data(**kwargs)
        context["counties"] = County.objects.all()
        context['universities'] = University.objects.annotate(accepted_review_count=Count('faculties_set__reviews_set', filter=Q(faculties_set__reviews_set__status=Review.StatusChoices.ACCEPTED)))

        return context
