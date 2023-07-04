from abc import ABC, abstractmethod

import logging

from landbot_challenge.task_queue.worker.tasks.task_definitions import send_email_task

logger = logging.getLogger(__name__)


class BaseChannelService(ABC):
    @abstractmethod
    def send(self):
        pass


class EmailChannel(BaseChannelService):
    @staticmethod
    def notify(description: str):
        send_email_task.apply_async(args=(description, description))


class SlackChannel(BaseChannelService):
    @staticmethod
    def notify(description: str):
        logger.info(f"Sending notification with {description} on Slack")
