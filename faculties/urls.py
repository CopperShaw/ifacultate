from django.urls import path

from faculties.views import FacultyDetailView, add_to_fav, fav_faculties

urlpatterns = [
    path(
        "universitati/<slug:slug_university>/<slug:slug_faculty>",
        FacultyDetailView.as_view(),
        name="faculty",
    ),
    path("fav-faculties/", fav_faculties, name="fav-faculties"),
    path("add-to-fav/<uuid:faculty_id>/", add_to_fav, name="add-to-fav"),
]
