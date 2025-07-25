from product_pipeline.notifications.base import NotificationChannel
from product_pipeline.utils.logging import get_logger

logger = get_logger("EmailNotification")


class EmailNotification(NotificationChannel):
    def __init__(self, config: dict):
        self.config = config

    def notify(self, product):
        msg = f"Sending email notification for product '{product.name}' with config {self.config}."
        logger.info(msg)
        print(f"[Email] {msg}")
