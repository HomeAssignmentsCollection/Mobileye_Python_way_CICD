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

        # Simulate SMTP connection for testing
        import smtplib

        try:
            with smtplib.SMTP(
                self.config.get("smtp_server"), self.config.get("port", 587)
            ) as server:
                # In a real implementation, you would send the email here
                # server.starttls()
                # server.login(username, password)
                # server.send_message(message)
                pass
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
