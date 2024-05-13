# import json
import os
import requests
from datetime import datetime, timedelta, timezone
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def check_periodicity_and_report_scheduler():
    """Runs the scheduler for periodic task check_periodicity_and_report."""
    schedule, create = IntervalSchedule.objects.get_or_create(
        every=3,
        period=IntervalSchedule.MINUTES,
    )

    PeriodicTask.objects.create(
        interval=schedule,  # we create this above
        name='Check periodicity and report',  # simple describes this periodic task
        task='core.tasks.check_periodicity_and_report',  # name of the task
        # args=json.dumps(['arg1', 'arg2']),
        # kwargs=json.dumps({
        #     'be_careful': True,
        # }),
        expires=datetime.now(timezone.utc) + timedelta(minutes=3),
    )


class MyTelegramBot:
    """Telegram bot for sending messages about periodicity habits."""

    URL = 'https://api.telegram.org/bot'
    TOKEN = os.getenv('TOKEN_TELEGRAM')

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': os.getenv('ID_TELEGRAM'),
                'text': text,
            }
        )
