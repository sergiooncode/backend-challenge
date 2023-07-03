import uuid

from django.db import models

from landbot_challenge.channels.models import Channel
from landbot_challenge.topics.models import Topic


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.ForeignKey(Topic, null=False, on_delete=models.PROTECT,
                              unique=True)
    channel = models.ForeignKey(Channel, null=False, on_delete=models.PROTECT)

    class Meta:
        db_table = "notifications"
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
