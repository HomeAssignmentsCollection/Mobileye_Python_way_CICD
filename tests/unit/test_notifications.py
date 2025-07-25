import pytest
from unittest.mock import patch, MagicMock
from src.product_pipeline.notifications.email import EmailNotification
from src.product_pipeline.notifications.slack import SlackNotification
from src.product_pipeline.notifications.base import NotificationChannel


class TestNotificationChannel:
    """Test the abstract base class for notification channels."""

    def test_abstract_methods(self):
        """Test that abstract methods are properly defined."""
        # Should not be able to instantiate abstract class
        with pytest.raises(TypeError):
            NotificationChannel()


class TestEmailNotification:
    """Test email notification channel."""

    def test_email_notification_init(self):
        """Test email notification initialization."""
        config = {"smtp_server": "smtp.example.com", "port": 587}
        email_notif = EmailNotification(config=config)
        assert email_notif.config == config

    @patch("smtplib.SMTP")
    def test_email_notification_send(self, mock_smtp):
        """Test email notification sending."""
        config = {"smtp_server": "smtp.example.com", "port": 587}
        email_notif = EmailNotification(config=config)

        # Mock product
        mock_product = MagicMock()
        mock_product.name = "TestProduct"

        # Mock SMTP
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_smtp_instance

        email_notif.notify(mock_product)

        # Verify SMTP was called
        mock_smtp.assert_called_once_with("smtp.example.com", 587)


class TestSlackNotification:
    """Test Slack notification channel."""

    def test_slack_notification_init(self):
        """Test Slack notification initialization."""
        config = {"webhook_url": "https://hooks.slack.com/services/test"}
        slack_notif = SlackNotification(config=config)
        assert slack_notif.config == config

    @patch("requests.post")
    def test_slack_notification_send(self, mock_post):
        """Test Slack notification sending."""
        config = {"webhook_url": "https://hooks.slack.com/services/test"}
        slack_notif = SlackNotification(config=config)

        # Mock product
        mock_product = MagicMock()
        mock_product.name = "TestProduct"

        # Mock HTTP response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        slack_notif.notify(mock_product)

        # Verify HTTP POST was called
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[0][0] == "https://hooks.slack.com/services/test"
