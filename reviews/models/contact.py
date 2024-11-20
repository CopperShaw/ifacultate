from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField(max_length=2555)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(
        default=False
    )  # after the user was contacted set to True
