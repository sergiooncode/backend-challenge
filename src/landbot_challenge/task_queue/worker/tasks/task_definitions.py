import logging

from django.core.mail import send_mail

from landbot_challenge.task_queue.worker.app import app

logger = logging.getLogger(__name__)


@app.task
def send_email_task(
        subject: str,
        message: str
):
    logger.info("send_email_task", message="Send an email deferredly")
    send_mail(subject=subject, message=message)
