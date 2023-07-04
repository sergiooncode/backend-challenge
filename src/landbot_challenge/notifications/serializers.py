import logging
from http import HTTPStatus

from rest_framework import serializers
from rest_framework.response import Response

from landbot_challenge.channels.models import CHANNEL_TO_CHANNEL_IMPLEMENTATION_CLASS
from landbot_challenge.notifications.exceptions import LandbotUnexpectedError
from landbot_challenge.notifications.models import Notification

logger = logging.getLogger(__name__)


class NotificationsSerializer(serializers.Serializer):
    topic = serializers.CharField()
    description = serializers.CharField(max_length=100)

    def create(self, validated_data):
        topic_name = validated_data.get("topic")
        description = validated_data.get("description")
        try:
            notification_queryset = Notification.objects.filter(topic__name=topic_name)
            notification = notification_queryset.first()
            print(notification)
            CHANNEL_TO_CHANNEL_IMPLEMENTATION_CLASS[
                notification.channel.name].notify(description=description)
        except LandbotUnexpectedError as error:
            logger.info(f"Unexpected error")
            return Response({"detail": "Unexpected error"},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR)
