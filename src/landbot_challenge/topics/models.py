import uuid

from django.db import models


class TopicName(models.TextChoices):
    SALES = "Sales", "Sales"
    PRICING = "Pricing", "Pricing"


class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=15,
        choices=TopicName.choices,
        null=False,
        blank=False,
        default=None
    )

    class Meta:
        db_table = "topics"
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
