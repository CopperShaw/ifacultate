from django.shortcuts import render

from reviews.models import Review


def home_view(request):

    return render(
        request,
        "reviews/index.html",
        {"recent_reviews": Review.recent.all(), "no_reviews": Review.objects.count()},
    )
