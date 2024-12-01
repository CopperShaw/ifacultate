from django.contrib import admin
from django.db import models
from django import forms
from reviews.models import Contact, Review

class CustomAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea(attrs={'rows':4, 'cols':40})},
    }

@admin.register(Review)
class ReviewModelAdmin(CustomAdmin):
    list_display = (
        "title",
        "faculty",
        "user_type",
        "created_at",
        "status",
        "publish",
    )



@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "email",
        "created_at",
        "completed",
    )