from typing import Any

from django.views.generic import DetailView

from faculties.models.faculty import Faculty
from universities.models.university import University


class UniversityDetailView(DetailView):
    model = University
    template_name = "universities/university_detail.html"
    slug_url_kwarg = "slug_university"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        university = kwargs.get("object")
        context["faculties"] = university.faculties_set.all()
        return context
