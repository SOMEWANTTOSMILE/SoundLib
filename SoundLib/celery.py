from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoundLib.settings')

app = Celery('SoundLib')  # Replace 'your_project' with your project's name.

# Configure Celery using settings from Django settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load tasks from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_premium': {
        'task': 'premium.tasks.check_premium',
        'schedule': crontab(minute='*/1')
    },
    'subscription_reminder': {
        'task': 'premium.tasks.subscription_reminder',
        'schedule': crontab(minute='*/1')
    }
}
