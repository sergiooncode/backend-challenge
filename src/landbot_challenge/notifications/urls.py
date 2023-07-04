from django.urls import path

from landbot_challenge.notifications.views import NotificationsViewSet

urlpatterns = [
    path(
        r"notification/",
        NotificationsViewSet.as_view({"post": "post"}),
        name="notifications",
    )
]
