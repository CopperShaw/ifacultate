from typing import Any

from django.views.generic import ListView

from faculties.models import County
from universities.models.university import University


class UniversityListView(ListView):
    model = University
    template_name = "university_list.html"  # default
    context_object_name = "universities"  # Optional, default is 'object_list'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UniversityListView, self).get_context_data(**kwargs)
        context["counties"] = County.objects.all()
        return context
