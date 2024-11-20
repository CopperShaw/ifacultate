from django.shortcuts import redirect, render

from reviews.forms import ReviewForm
from universities.models import University


def add_review(request, slug_university=None, slug_faculty=None):
    form = ReviewForm(slug_university=slug_university, slug_faculty=slug_faculty)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("home")
        else:
            form = ReviewForm(
                request.POST, slug_university=slug_university, slug_faculty=slug_faculty
            )

    universities = University.objects.all()

    if slug_university and slug_faculty:
        universities = universities.exclude(slug=slug_university)
        university = University.objects.get(slug=slug_university)

        return render(
            request,
            "reviews/review_create.html",
            {
                "form": form,
                "universities": universities,
                "faculties": university.faculties_set.exclude(slug=slug_faculty),
            },
        )

    else:
        return render(
            request,
            "reviews/review_create.html",
            {
                "form": form,
                "universities": universities,
            },
        )
