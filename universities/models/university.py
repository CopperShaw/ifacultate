import uuid

from autoslug import AutoSlugField
from django.db import models



class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, db_index=True)
    is_private = models.BooleanField(default=False)
    county = models.ForeignKey(
        "faculties.County",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    founded = models.CharField(max_length=128)
    total_reviews = models.IntegerField(default=0)
    url = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        verbose_name = "Universitate"
        verbose_name_plural = "Universități"

    def __str__(self) -> str:
        return self.name
