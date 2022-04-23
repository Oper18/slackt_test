from django.db import models


class Container(models.Model):
    number = models.IntegerField(verbose_name="container number")
    size = models.CharField(verbose_name="size of container", max_length=128)
    created_at = models.DateTimeField(
        verbose_name="created date", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="updated date", auto_now=True
    )

    class Meta:
        verbose_name = "Container"
        verbose_name_plural = "Containers"
