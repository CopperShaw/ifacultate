from django.views.generic import DetailView
from reviews.models import Review

class ReviewDetailView(DetailView):
    model = Review
    # template_name = 'review_detail.html'
    context_object_name = 'review'
