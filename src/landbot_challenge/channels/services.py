from abc import ABC, abstractmethod

import logging

from django.core.mail import send_mail

logger = logging.getLogger(__name__)


class BaseChannelService(ABC):
    @abstractmethod
    def send(self):
        pass


class EmailChannel(BaseChannelService):
    @staticmethod
    def notify(description: str):
        send_mail(subject=description, message=description)


class SlackChannel(BaseChannelService):
    @staticmethod
    def notify(description: str):
        logger.info(f"Sending notification with {description} on Slack")
