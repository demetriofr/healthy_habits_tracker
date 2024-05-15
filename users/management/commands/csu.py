from os import getenv
from dotenv import load_dotenv
from django.core.management import BaseCommand

from users.models import User


load_dotenv()


class Command(BaseCommand):
    """Create SuperUser."""

    def handle(self, *args, **options):
        """
        Handle function to create a superuser with environment variables.
        """

        # Creating a superuser with the provided environment variables
        csu = User.objects.create(
            email=getenv('CSU_EMAIL'),
            first_name=getenv('CSU_FIRST_NAME'),
            last_name=getenv('CSU_LAST_NAME'),
            user_id_telegram=getenv('CSU_ID_TELEGRAM'),
            is_staff=True,
            is_superuser=True,
        )

        # Setting the password for the superuser
        csu.set_password(getenv('CSU_PASSWORD'))

        csu.save()
