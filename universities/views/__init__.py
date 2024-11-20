from universities.views.uni_detail import UniversityDetailView
from universities.views.uni_list import UniversityListView

from .htmx_views import universities_search_result

__all__ = [
    UniversityListView,
    UniversityDetailView,
    universities_search_result,
]
