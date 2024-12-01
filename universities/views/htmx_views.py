import json

from django.db.models import Count, Q
from django.shortcuts import render

from universities.models import University
from reviews.models import Review


def universities_search_result(request):
    query = request.GET.get("search", "")
    county = request.GET.getlist("county", "")
    sort = request.GET.get("sort", "")
    stat = request.GET.get("stat", "")
    privat = request.GET.get("privat", "")

    universities = University.objects.all().annotate(accepted_review_count=Count('faculties_set__reviews_set', filter=Q(faculties_set__reviews_set__status=Review.StatusChoices.ACCEPTED)))

    if query:
        universities = universities.filter(name__icontains=query)

    if county:
        universities = universities.filter(county__pk__in=county)

    if stat and privat:
        pass
    elif stat:
        universities = universities.filter(is_private=False)
    elif privat:
        universities = universities.filter(is_private=True)

    if sort:
        if sort == "sort-ascending":
            universities = universities.order_by("-accepted_review_count")
        else:
            universities = universities.order_by("accepted_review_count")

    if not (county or query):
        universities = universities

    return render(
        request,
        "universities/partials/search_results.html",
        {"universities": universities},
    )
