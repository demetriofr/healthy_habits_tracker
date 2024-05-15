from math import ceil
from datetime import datetime, timezone
from celery import shared_task

from .models import Habit
from .services import TelegramBotSender


@shared_task
def check_periodicity_and_report():
    """Checks the periodicity of habits and reports user owner of the habit."""

    # gets all habits witt periodicity
    habits = Habit.objects.filter(periodicity__isnull=False)

    # rounds the current time to the nearest second
    current_time_rounded = ceil(datetime.now().timestamp())

    for habit in habits:

        # gets the last time the habit was executed
        last_execute_time = habit.executed_time if habit.executed_time else habit.created_at

        # rounds to the nearest second
        last_execute_time_rounded = ceil(last_execute_time.timestamp())

        # converts days to seconds
        habit_periodicity = habit.periodicity * 24 * 60 * 60

        # adds the periodicity to the last time the habit was executed
        last_execute_time_plus_habit_periodicity = last_execute_time_rounded + habit_periodicity

        # gets the delta between the current time and the last time the habit was executed
        delta = (abs(last_execute_time_plus_habit_periodicity - current_time_rounded))

        # send message if delta is less or equal than 1 minute
        if delta <= 1 * 60:

            # updates executed time to the habit model
            habit.executed_time = datetime.now(timezone.utc)
            habit.save()

            # creates message to send
            text = f'Пришло время выполнить привычку! \nЯ буду {habit.action} в {habit.time} в {habit.place}.'

            # sends message to habit owner
            telegram_bot_sender = TelegramBotSender()
            chat_id = Habit.objects.get(id=habit.id).user.user_id_telegram  # gets user id telegram
            telegram_bot_sender.send_message(chat_id, text)
