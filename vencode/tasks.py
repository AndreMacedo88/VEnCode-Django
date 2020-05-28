# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from time import sleep


@shared_task
def sleepy(duration, x, y):
    sleep(duration)
    return x + y
