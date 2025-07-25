from product_pipeline.notifications.base import NotificationChannel
from product_pipeline.utils.logging import get_logger

logger = get_logger("SlackNotification")


class SlackNotification(NotificationChannel):
    def __init__(self, config: dict):
        self.config = config

    def notify(self, product):
        msg = f"Sending Slack notification for product '{product.name}' with config {self.config}."
        logger.info(msg)
        print(f"[Slack] {msg}")
