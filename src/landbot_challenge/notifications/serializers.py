from rest_framework import serializers


class NotificationsSerializer(serializers.Serializer):
    topic = serializers.CharField()
    description = serializers.CharField(max_length=100)
