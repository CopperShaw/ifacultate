from typing import Any

from django.views.generic import DetailView

from faculties.models.faculty import Faculty
from reviews.models.review import Review


class FacultyDetailView(DetailView):
    model = Faculty
    template_name = "faculties/faculty_detail.html"
    slug_url_kwarg = "slug_faculty"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        faculty = kwargs.get("object")
        context["reviews"] = Review.accepted.filter(faculty=faculty)
        return context
