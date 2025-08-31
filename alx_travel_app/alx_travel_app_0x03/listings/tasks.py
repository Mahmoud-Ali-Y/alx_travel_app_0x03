from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(to_email, booking_id):
    subject = "Booking Confirmation"
    message = f"Thank you for your booking! Your booking ID is {booking_id}."
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, [to_email])
    return f"Sent booking confirmation to {to_email} for booking {booking_id}"