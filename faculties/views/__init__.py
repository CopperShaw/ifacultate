from faculties.views.faculty_detail import FacultyDetailView

from .add_to_fav import add_to_fav
from .faculty_list import fav_faculties

__all__ = [
    FacultyDetailView,
    fav_faculties,
    add_to_fav,
]
