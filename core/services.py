# import json
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
