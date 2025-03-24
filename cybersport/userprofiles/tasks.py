from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_verification_email(email, code):
    subject = "Подтверждение Email"
    message = f"Ваш код подтверждения: {code}. Он действителен в течение 10 минут."
    from_email = "noreply@yourdomain.com"
    send_mail(subject, message, from_email, [email])
