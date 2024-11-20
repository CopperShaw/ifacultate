from django.contrib import admin

from normalaccount.models.custom_user import CustomUser


@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "date_joined",
        "t_and_c",
    )
