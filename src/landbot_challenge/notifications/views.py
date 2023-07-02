from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from landbot_challenge.notifications.serializers import NotificationsSerializer


class NotificationsViewSet(viewsets.GenericViewSet):
    serializer_class = NotificationsSerializer

    def post(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response("", status=HTTPStatus.CREATED)
