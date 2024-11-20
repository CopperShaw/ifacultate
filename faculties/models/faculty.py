import uuid

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from reviews.models import Review


class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, db_index=True)
    university = models.ForeignKey(
        "universities.University",
        on_delete=models.CASCADE,
        related_name="faculties_set",
    )
    county = models.ForeignKey(
        "County", on_delete=models.DO_NOTHING, related_name="faculties_set"
    )
    reviews_number = models.IntegerField(default=0)
    rating = models.DecimalField(decimal_places=1, max_digits=2, null=True, default=0.0)
    favorites = models.ManyToManyField(
        get_user_model(), related_name="favorites", default=None, blank=True
    )
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        verbose_name = "Facultate"
        verbose_name_plural = "Facultăți"

    def __str__(self) -> str:
        return self.name


@receiver(post_save, sender=Review)
def update_reviews_number(sender, instance, created, **kwargs):
    if created:
        faculty = instance.faculty
        faculty.reviews_number += 1
        faculty.save()


@receiver(pre_delete, sender=Review)
def update_reviews_number_on_delete(sender, instance, **kwargs):
    faculty = instance.faculty
    faculty.reviews_number -= 1
    faculty.save()
