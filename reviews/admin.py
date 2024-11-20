from django.contrib import admin

from reviews.models import Contact, Review

# Register your models here.


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
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