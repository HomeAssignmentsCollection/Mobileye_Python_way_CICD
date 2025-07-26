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

        # Simulate HTTP request for testing
        import requests

        try:
            response = requests.post(
                self.config.get("webhook_url"),
                json={"text": f"Product {product.name} has been processed"},
            )
            response.raise_for_status()
        except Exception as e:
            logger.error(f"Failed to send Slack notification: {e}")
