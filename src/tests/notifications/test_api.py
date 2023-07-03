from http import HTTPStatus
from unittest import mock

import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


def test_should_notify_by_email_when_topic_is_sales(notification_with_sales_topic_and_email_channel):
    client = APIClient()

    with mock.patch("landbot_challenge.channels.services.send_mail") as mocked_mail:
        response = client.post(
            "/api/notify/", data={"topic": "Sales", "description": "A description"}
        )

        mocked_mail.assert_called_once_with(
            subject='A description', message='A description'
        )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == ""


def test_should_notify_by_slack_when_topic_is_pricing(notification_with_pricing_topic_and_slack_channel):
    client = APIClient()

    response = client.post(
        "/api/notify/", data={"topic": "Pricing", "description": "A description"}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == ""
