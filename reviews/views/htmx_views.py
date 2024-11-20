from django.shortcuts import HttpResponse, render

from reviews.models import Review
from universities.models import University


def faculties_dropdown(request):
    university_id = request.GET.get("university")
    university = University.objects.get(pk=university_id)
    return render(
        request,
        "reviews/partials/faculty_dropdown.html",
        {
            "faculties": university.faculties_set.all(),
        },
    )


def add_review_to_fav(request, review_id):
    user = request.user
    review = Review.objects.get(pk=review_id)

    if review in user.favorite_reviews.all():
        user.favorite_reviews.remove(review_id)
        return HttpResponse("♡ Adaugă la favorite")
    else:
        user.favorite_reviews.add(review_id)
        return HttpResponse("❤️ Elimină de la favorite")


def get_reviews(request, faculty_id):
    sort = request.GET.get("sort", "")
    reviews = Review.accepted.filter(faculty=faculty_id)

    if sort:
        if sort == "sort-new":
            reviews = reviews.order_by("-created_at")

        elif sort == "sort-old":
            reviews = reviews.order_by("created_at")

    return render(request, "reviews/review_list.html", {"reviews": reviews})


def future_students_partial(request):
    return render(request, "reviews/partials/future_students.html")


def graduates_partial(request):
    return render(request, "reviews/partials/graduates.html")
