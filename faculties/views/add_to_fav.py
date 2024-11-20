from django.shortcuts import HttpResponse

from faculties.models import Faculty


def add_to_fav(request, faculty_id):
    user = request.user
    faculty = Faculty.objects.get(pk=faculty_id)

    if faculty in user.favorites.all():
        user.favorites.remove(faculty_id)
        return HttpResponse("♡ Adaugă la favorite")
    else:
        user.favorites.add(faculty_id)
        return HttpResponse("❤️ Elimină de la favorite")
