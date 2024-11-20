from django.shortcuts import render


def my_reviews_view(request):
    my_reviews = request.user.my_reviews.all()

    return render(request, "reviews/partials/my_reviews.html", {"reviews": my_reviews})


def my_favorite_reviews_view(request):
    my_reviews = request.user.favorite_reviews.all()

    return render(
        request,
        "reviews/partials/my_reviews.html",
        {"reviews": my_reviews if my_reviews else None, "fav": True},
    )
