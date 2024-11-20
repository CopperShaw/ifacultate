from django.contrib import admin

from universities.models.university import University


# Register your models here.
class UniversityAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_private", "url"]


admin.site.register(University, UniversityAdmin)
