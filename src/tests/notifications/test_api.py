from http import HTTPStatus
from unittest import mock
from unittest.mock import call

import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


def test_should_notify_by_email_when_topic_is_sales(notification_with_sales_topic_and_email_channel):
    client = APIClient()

    with mock.patch(
            "landbot_challenge.channels.services.send_email_task.apply_async"
    ) as mocked_send_mail_task:
        response = client.post(
            "/api/notification/", data={"topic": "Sales", "description": "A description"}
        )

        assert mocked_send_mail_task.call_args == call(args=('A description', 'A description'))

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == ""


def test_should_notify_by_slack_when_topic_is_pricing(notification_with_pricing_topic_and_slack_channel):
    client = APIClient()

    response = client.post(
        "/api/notification/", data={"topic": "Pricing", "description": "A description"}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == ""
