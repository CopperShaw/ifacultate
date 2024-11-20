from django.db import models


class County(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Județ"
        verbose_name_plural = "Județe"
