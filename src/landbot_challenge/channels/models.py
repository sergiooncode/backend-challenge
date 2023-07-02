import uuid

from django.db import models

from landbot_challenge.channels.services import EmailChannel, SlackChannel


class ChannelName(models.TextChoices):
    EMAIL = "Email", "Email"
    SLACK = "Slack", "Slack"


CHANNEL_TO_CHANNEL_IMPLEMENTATION_CLASS = {
    ChannelName.EMAIL.value: EmailChannel,
    ChannelName.SLACK.value: SlackChannel
}


class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=20,
        choices=ChannelName.choices,
        null=False,
        blank=False,
        default=None
    )

    class Meta:
        db_table = "channels"
        verbose_name = "Channel"
        verbose_name_plural = "Channels"
