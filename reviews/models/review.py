import uuid

from django.contrib.auth import get_user_model
from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class AcceptedManager(models.Manager):
    """
    Return a QuerySet with the accepted reviews.
    """

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Review.StatusChoices.ACCEPTED)


class RecentManager(models.Manager):
    """
    Return a QuerySet containing the three latest reviews.
    """

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().order_by("-created_at")[:3]


class Review(models.Model):
    class StatusChoices(models.TextChoices):
        SUBMITED = "SUB", "Trimis"
        REVIEWING = "REV", "În așteptare"
        ACCEPTED = "ACC", "Acceptat"
        REJECTED = "REJ", "Respins"

    class UserTypeChoices(models.TextChoices):
        NADA = "", "Absolvent / Student"
        GRADUATE = "GR", "Absolvent"
        STUDENT = "ST", "Student"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name="my_reviews",
        blank=True,
        null=True,
    )
    favorites = models.ManyToManyField(
        get_user_model(), related_name="favorite_reviews", default=None, blank=True
    )
    university = models.ForeignKey(
        "universities.University",
        on_delete=models.DO_NOTHING,
        null=True,
    )
    faculty = models.ForeignKey(
        "faculties.Faculty",
        on_delete=models.SET_NULL,
        null=True,
        related_name="reviews_set",
    )
    grad_promo = models.CharField(max_length=9, default="")
    user_type = models.CharField(
        max_length=2,
        choices=UserTypeChoices.choices,
        blank=True,
    )
    title = models.CharField(max_length=255, validators=[MinLengthValidator(10)])
    pro = models.CharField(max_length=5555, validators=[MinLengthValidator(50)])
    against = models.CharField(max_length=5555, validators=[MinLengthValidator(50)])
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    status = models.CharField(
        max_length=3,
        choices=StatusChoices.choices,
        default=StatusChoices.SUBMITED,
    )
    advice = models.CharField(max_length=1000, validators=[MinLengthValidator(50)])
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    accepted = AcceptedManager()
    recent = RecentManager()

    class Meta:
        verbose_name = "Părere"
        verbose_name_plural = "Păreri"
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title[:10] + "..."

    @property
    def formatted_date(self):
        return self.created_at.strftime("%d.%m.%Y")

    # def get_absolute_url(self):
    #     return reverse("review_detail", args=[self.id])
