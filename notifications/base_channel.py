from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def notify(self, product):
        """Method for sending a notification about the product."""
        pass
