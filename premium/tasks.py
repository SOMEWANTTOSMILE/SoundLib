from celery import shared_task
import time
import os
import django
from datetime import datetime, timedelta, timezone
from django.conf import settings
from django.core.mail import send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SoundLib.settings")
django.setup()


@shared_task
def check_premium():
    from premium.models import UserSubscription
    time_now = datetime.now(timezone.utc)
    user_sub = UserSubscription.objects.filter(is_active=True)
    for user in user_sub:
        time_difference = user.expiring_on - time_now
        if time_difference > timedelta(days=1):
            print(f'The user has been verified for subscription activity {user.user}')
        else:
            print(f'The user has not passed the subscription activity check {user.user}')
            user.is_active = False
            user.save()


@shared_task
def subscription_reminder():
    from premium.models import UserSubscription
    time_now = datetime.now(timezone.utc)
    user_sub = UserSubscription.objects.filter(is_active=True)
    for user in user_sub:
        time_difference = user.expiring_on - time_now
        if time_difference == timedelta(days=1) and user.is_notificated is False:
            send_mail(
                'Подписка скоро истечет',
                f'Подписка истечет {user.expiring_on}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.user]
            )
            user.is_notificated = True
            user.save()

