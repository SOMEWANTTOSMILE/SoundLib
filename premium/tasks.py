from celery import shared_task
import time


@shared_task
def some_task():
    time.sleep(5)
    return "it`s work"


@shared_task
def some_scheduled_task():
    return "schedule is works"
