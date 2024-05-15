import os
import requests
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def schedule_for_check_periodicity_and_report():
    """Runs the scheduler for periodic task check_periodicity_and_report."""

    schedule, create = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.MINUTES,
    )

    PeriodicTask.objects.create(
        interval=schedule,  # we create this above
        name='Check periodicity and report',  # simple describes this periodic task
        task='core.tasks.check_periodicity_and_report',  # name of the task
    )


class TelegramBotSender:
    """Telegram bot for sending messages about periodicity habits."""

    URL = 'https://api.telegram.org/bot'
    TOKEN = os.getenv('TOKEN_TELEGRAM')

    def send_message(self, chat_id, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text,
            }
        )
