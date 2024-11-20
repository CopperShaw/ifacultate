from django.urls import path

from universities.views import (UniversityDetailView, UniversityListView,
                                universities_search_result)

urlpatterns = [
    path("universitati/", UniversityListView.as_view(), name="universitati"),
    path(
        "universitati/<slug:slug_university>",
        UniversityDetailView.as_view(),
        name="university",
    ),
    path("search-uni/", universities_search_result, name="search-uni"),
]
