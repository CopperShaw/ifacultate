from .about_view import AboutView
from .contact_view import ContactSent, ContactView
from .cookies import CookiesView
from .date import DateView
from .faq import FAQView
from .home_view import home_view
from .htmx_views import (add_review_to_fav, faculties_dropdown,
                         future_students_partial, get_reviews,
                         graduates_partial)
from .my_reviews import my_favorite_reviews_view, my_reviews_view
from .review_crud import add_review
from .search_results import search_results_view
from .t_and_c import TermsView
from .review_detail import ReviewDetailView

__all__ = [
    home_view,
    add_review,
    search_results_view,
    faculties_dropdown,
    get_reviews,
    AboutView,
    ContactView,
    ContactSent,
    CookiesView,
    DateView,
    TermsView,
    my_reviews_view,
    my_favorite_reviews_view,
    add_review_to_fav,
    future_students_partial,
    graduates_partial,
    FAQView,
    ReviewDetailView,
]
