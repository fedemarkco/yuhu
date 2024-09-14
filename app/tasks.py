from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_task_notification(email, subject, message):
    send_mail(
        subject,
        message,
        settings.SENDER,
        [email],
        fail_silently=False,
    )
