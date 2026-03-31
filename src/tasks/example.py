import logging

from src.core.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(bind=True, max_retries=3, default_retry_delay=5)
def add(self, x: int, y: int) -> int:
    return x + y


@celery_app.task(bind=True, max_retries=3, default_retry_delay=60)
def send_welcome_email(self, email: str, username: str) -> dict:
    try:
        logger.info(f"Sending welcome email to {username} at {email}")
        # In production: call SendGrid, SES, Resend, etc. here
        return {"status": "sent", "recipient": email}
    except Exception as exc:
        raise self.retry(exc=exc)