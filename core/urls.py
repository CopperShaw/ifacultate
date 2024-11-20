from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("normalaccount.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("reviews.urls")),
    path("", include("universities.urls")),
    path("", include("faculties.urls")),
]
