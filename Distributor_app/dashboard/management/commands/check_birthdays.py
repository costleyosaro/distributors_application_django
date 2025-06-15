from django.core.management.base import BaseCommand
from django.utils.timezone import now
from django.core.mail import send_mail
from django.conf import settings
from users.models import CustomUser  # ✅ Use your actual custom user model
from dashboard.models import Notification  # ✅ Adjust if Notification is somewhere else

class Command(BaseCommand):
    help = "Send birthday messages and notifications to users"

    def handle(self, *args, **kwargs):
        today = now().date()
        users_with_birthday = CustomUser.objects.filter(
            date_of_birth__month=today.month,
            date_of_birth__day=today.day
        )

        for user in users_with_birthday:
            message = f"🎂 Happy Birthday {user.username or user.name}! Wishing you joy and success. — From Chiamo Multitrade Developers Team 🎉"

            # Create an in-app notification
            Notification.objects.create(
                user=user,
                message=message,
                notification_type="birthday"
            )

            # Send an email
            send_mail(
                subject="🎉 Happy Birthday from Chiamo Multitrade!",
                message=message,
                from_email="no-reply@chiamo.ng",
                recipient_list=[user.email],
                fail_silently=False,
            )

        self.stdout.write(self.style.SUCCESS("🎂 Birthday notifications and emails sent successfully."))
