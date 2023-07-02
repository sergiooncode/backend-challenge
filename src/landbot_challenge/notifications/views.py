from rest_framework import viewsets

from landbot_challenge.notifications.serializers import NotificationsSerializer


class NotificationsViewSet(viewsets):
    serializer_class = NotificationsSerializer

    def create(self):
        pass
