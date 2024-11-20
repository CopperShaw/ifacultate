from django.urls import path

from .views import (AboutView, ContactSent, ContactView, CookiesView, DateView,
                    FAQView, TermsView, add_review, add_review_to_fav,
                    faculties_dropdown, future_students_partial, get_reviews,
                    graduates_partial, home_view, my_favorite_reviews_view,
                    my_reviews_view, search_results_view)

urlpatterns = [
    path("", home_view, name="home"),
    path(
        "universitati/adauga",
        add_review,
        name="add-review",
    ),
    path(
        "universitati/<slug:slug_university>/<slug:slug_faculty>/adauga",
        add_review,
        name="add-review",
    ),
    path("faculties-dropdown/", faculties_dropdown, name="faculties-dropdown"),
    path("despre/", AboutView.as_view(), name="about"),
    path("intrebari-frecvente/", FAQView.as_view(), name="faq"),
    path("prelucrare-date/", DateView.as_view(), name="date"),
    path("termeni-conditii/", TermsView.as_view(), name="t_and_c"),
    path("cookies/", CookiesView.as_view(), name="cookies"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("mesaj/<int:pk>/", ContactSent.as_view(), name="contact-sent"),
    path("search/results/", search_results_view, name="search-results"),
    path("my-reviews/", my_reviews_view, name="my-reviews"),
    path("my-fave-reviews/", my_favorite_reviews_view, name="my-fave-reviews"),
    path(
        "add-review-to-fav/<uuid:review_id>/",
        add_review_to_fav,
        name="add-review-to-fav",
    ),
    path("future-students/", future_students_partial, name="future-students"),
    path("graduates/", graduates_partial, name="graduates"),
    path("reviews/<uuid:faculty_id>", get_reviews, name="get-reviews"),
]
