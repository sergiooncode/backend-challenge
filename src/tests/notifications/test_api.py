from http import HTTPStatus

from rest_framework.test import APIClient


def test_should_notify_by_email_when_topic_is_sales():
    client = APIClient()

    response = client.post(
        "/api/notify/", data={"topic": "Sales", "description": "A description"}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == ""
