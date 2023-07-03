from rest_framework import serializers

from landbot_challenge.channels.models import CHANNEL_TO_CHANNEL_IMPLEMENTATION_CLASS
from landbot_challenge.notifications.models import Notification


class NotificationsSerializer(serializers.Serializer):
    topic = serializers.CharField()
    description = serializers.CharField(max_length=100)

    def create(self, validated_data):
        topic_name = validated_data.get("topic")
        description = validated_data.get("description")
        notification = Notification.objects.filter(topic__name=topic_name).first()
        CHANNEL_TO_CHANNEL_IMPLEMENTATION_CLASS[
            notification.channel.name].notify(description=description)
