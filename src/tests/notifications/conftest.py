import pytest

from landbot_challenge.channels.models import Channel, ChannelName
from landbot_challenge.notifications.models import Notification
from landbot_challenge.topics.models import Topic, TopicName


@pytest.fixture
def notification_with_sales_topic_and_email_channel():
    topic = Topic.objects.create(name=TopicName.SALES.value)
    channel = Channel.objects.create(name=ChannelName.EMAIL.value)
    Notification.objects.create(topic=topic, channel=channel)


@pytest.fixture
def notification_with_pricing_topic_and_slack_channel():
    topic = Topic.objects.create(name=TopicName.PRICING.value)
    channel = Channel.objects.create(name=ChannelName.SLACK.value)
    Notification.objects.create(topic=topic, channel=channel)
