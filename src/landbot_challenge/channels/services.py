from abc import ABC, abstractmethod


class BaseChannelService(ABC):
    @abstractmethod
    def send(self):
        pass


class EmailChannel(BaseChannelService):
    def send(self):
        pass


class SlackChannel(BaseChannelService):
    def send(self):
        pass
