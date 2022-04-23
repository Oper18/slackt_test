from django.db import models


class Order(models.Model):
    container = models.ForeignKey(
        "product.Container",
        verbose_name="",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    client = models.CharField(
        verbose_name="client name",
        max_length=255,
    )
    created_at = models.DateTimeField(
        verbose_name="created date", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="updated date", auto_now=True
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
