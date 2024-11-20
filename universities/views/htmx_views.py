from django.db.models import OuterRef, Subquery, Sum
from django.shortcuts import render

from faculties.models import Faculty
from universities.models import University


def universities_search_result(request):
    query = request.GET.get("search", "")
    county = request.GET.getlist("county", "")
    sort = request.GET.get("sort", "")
    stat = request.GET.get("stat", "")
    privat = request.GET.get("privat", "")

    universities = University.objects.all()

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
            universities = universities.order_by("-total_reviews")
        else:
            universities = universities.order_by("total_reviews")

    if not (county or query):
        universities = universities

    return render(
        request,
        "universities/partials/search_results.html",
        {"universities": universities},
    )
