from django.db.models import Q
from django.shortcuts import render
from django.utils.html import format_html

from faculties.models import Faculty


def search_results_view(request):
    query = request.GET.get("search", "")

    all_faculties = Faculty.objects.all()
    if query:
        faculties = all_faculties.filter(
            Q(name__icontains=query) | Q(slug__icontains=query)
        )
        highlighted_faculties = [
            {
                "name": highlight_matched_text(faculty.name, query),
                "university": faculty.university,
                "slug": faculty.slug,
            }
            for faculty in faculties
        ]
    else:
        highlighted_faculties = []

    context = {"faculties": highlighted_faculties}
    return render(request, "reviews/partials/search_results.html", context)


def highlight_matched_text(text, query):
    """
    Inserts html around the matched text.
    """
    start = text.lower().find(query.lower())
    if start == -1:
        return text
    end = start + len(query)
    highlighted = format_html('<span class="highlight">{}</span>', text[start:end])
    return format_html("{}{}{}", text[:start], highlighted, text[end:])
