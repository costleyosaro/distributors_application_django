from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from dashboard.models import Invoice, PaymentItem, Payment, Notification
from django.db.models import Sum
from datetime import date
from dashboard.models import Product, InvoiceItem
from django.core.mail import send_mail
from django.conf import settings
import re

User = get_user_model()

# 🧹 Remove emojis from emails
def strip_emojis(text):
    emoji_pattern = re.compile("[" 
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


# ✅ Safe email sender
def safe_send_mail(subject, message, recipient_email):
    try:
        send_mail(
            subject=subject,
            message=strip_emojis(message),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False,
        )
    except Exception as e:
        print("✉️ Email sending failed:", e)


# ✅ Notify users and email actor only
def notify_all_with_personalization(actor, personal_message, others_message, notification_type):
    for user in User.objects.all():
        Notification.objects.create(
            user=user,
            message=personal_message if user == actor else others_message,
            notification_type=notification_type
        )

    if actor.email:
        safe_send_mail(
            subject="Notification from Chiamo Multitrade Distributor Portal",
            message=personal_message,
            recipient_email=actor.email
        )


# ✅ New Distributor Registration
@receiver(post_save, sender=User)
def new_distributor_registered(sender, instance, created, **kwargs):
    if created:
        notify_all_with_personalization(
            actor=instance,
            personal_message="🎉 You just registered. Welcome aboard!",
            others_message=f"🆕 New distributor '{instance.username}' has just registered.",
            notification_type="new_registration"
        )


# ✅ Birthday Notification
@receiver(post_save, sender=User)
def check_birthday(sender, instance, **kwargs):
    if instance.date_of_birth and instance.date_of_birth == date.today():
        notify_all_with_personalization(
            actor=instance,
            personal_message="🎂 Happy Birthday to you! 🎉",
            others_message=f"🎂 Today is {instance.username}'s birthday! Wish them a great day! 🎉",
            notification_type="birthday"
        )


# ✅ Invoice Raised
@receiver(post_save, sender=Invoice)
def invoice_created(sender, instance, created, **kwargs):
    if created:
        notify_all_with_personalization(
            actor=instance.user,
            personal_message=f"🧾 You just raised an invoice with ID {instance.invoice_id}.",
            others_message=f"🧾 {instance.user.username} just raised an invoice with ID {instance.invoice_id}.",
            notification_type="invoice_created"
        )


# ✅ Payment Success
@receiver(post_save, sender=PaymentItem)
def payment_successful(sender, instance, created, **kwargs):
    if created and instance.payment.status == "success":
        user = instance.payment.user
        invoice_id = instance.payment.invoice.invoice_id
        notify_all_with_personalization(
            actor=user,
            personal_message=f"💰 You just completed payment for Invoice {invoice_id}.",
            others_message=f"💰 {user.username} just completed payment for Invoice {invoice_id}.",
            notification_type="payment_success"
        )


# ✅ Bonus Product Eligibility
@receiver(post_save, sender=Invoice)
def check_bonus_product(sender, instance, created, **kwargs):
    if not created:
        return

    food_product_names = [
        "7 to 7 Choco Gold x 24",
        "7 to 7 COCONUT GOLD x 24",
        "7 TO 7 COOKIES GOLD x 24",
        "7 TO 7 MILKY GOLD x 24"
    ]
    threshold_quantity = 25
    bonus_product = "TOO CLEAN DETERGENT 350g"
    eligible = False

    for item in instance.items.all():
        cleaned_name = item.product_name.strip().upper()
        if cleaned_name in [name.upper() for name in food_product_names] and item.quantity >= threshold_quantity:
            eligible = True
            break

    if eligible:
        Notification.objects.create(
            user=instance.user,
            message=f"🎉 Hurray {instance.user.username}! You've been gifted a {bonus_product}! 🎁",
            notification_type="bonus_product"
        )
        if instance.user.email:
            safe_send_mail(
                subject="You've earned a bonus!",
                message="🎉 You earned a bonus! Check your dashboard for details.",
                recipient_email=instance.user.email
            )


# ✅ Incentive Achieved
@receiver(post_save, sender=Invoice)
def check_incentive_eligibility(sender, instance, **kwargs):
    total_spent = Payment.objects.filter(
        user=instance.user,
        added_at__month=now().month
    ).aggregate(total=Sum("grand_total"))["total"] or 0

    if total_spent >= 15000000:
        notify_all_with_personalization(
            actor=instance.user,
            personal_message="🏆 You’ve achieved the ₦15M target! You qualify for the 1% incentive reward! 🎉",
            others_message=f"🏆 {instance.user.username} has achieved the ₦15M target and qualified for the 1% incentive reward! 🎉",
            notification_type="incentive"
        )
