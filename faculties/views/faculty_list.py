from django.shortcuts import render


def fav_faculties(request):
    favorite_faculties = request.user.favorites.all()

    return render(
        request,
        "faculties/partials/favorite_faculties.html",
        {"faculties": favorite_faculties},
    )
