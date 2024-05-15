from django.core.management import BaseCommand

from core.tasks import check_periodicity_and_report


class Command(BaseCommand):
    """Test launch check_periodicity_and_report."""

    def handle(self, *args, **options):

        check_periodicity_and_report()
