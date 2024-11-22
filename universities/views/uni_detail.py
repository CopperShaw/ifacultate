from typing import Any

from django.views.generic import DetailView
from django.db.models import Avg, Count, Value, Q, FloatField
from django.db.models.functions import Coalesce

from universities.models.university import University
from reviews.models.review import Review


class UniversityDetailView(DetailView):
    model = University
    template_name = "universities/university_detail.html"
    slug_url_kwarg = "slug_university"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        university = kwargs.get("object")

        related_faculties = university.faculties_set.all()
        related_faculties = related_faculties.annotate(accepted_review_count=Count('reviews_set', filter=Q(reviews_set__status=Review.StatusChoices.ACCEPTED)))
        related_faculties = related_faculties.annotate(rating=Coalesce(Avg('reviews_set__rating', filter=Q(reviews_set__status=Review.StatusChoices.ACCEPTED)), Value(0.0), output_field=FloatField()))
        context["faculties"] = related_faculties

        return context
