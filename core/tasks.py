from math import ceil
from datetime import datetime, timedelta
from celery import shared_task

from .models import Habit


@shared_task
def check_periodicity_and_report():
    """Checks the periodicity of habits and reports user owner of the habit."""

    results = []
    habits = Habit.objects.fillers(periodicity__isnull=False)  # gets all habits witt periodicity
    current_time_rounded = ceil(datetime.now().timestamp() / 60) * 60  # rounds the current time to the nearest minute
    for habit in habits:
        last_execute_time = habit.executed_time if habit.executed_time else habit.created_at

        # rounds the last_execute_time to the nearest minute
        last_execute_time_rounded = ceil(last_execute_time.timestamp() / 60) * 60
        habit_periodicity = habit.periodicity * 24 * 60  # converts days to minutes

        if last_execute_time_rounded + habit_periodicity == current_time_rounded:
            habit.executed_time = datetime.now()
            habit.save()
            results.append({
                'habit_id': habit.id,
                'user_id': habit.user_id,
                'executed_time': datetime.now(),
            })

        elif last_execute_time_rounded + habit_periodicity == current_time_rounded - 3 * 60:
            results.append({
                'habit_id': habit.id,
                'user_id': habit.user_id,
                'executed_time': datetime.now() - timedelta(minutes=3),
            })

    return results
