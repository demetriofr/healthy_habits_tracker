from django.core.management import BaseCommand

from core.services import MyTelegramBot


class Command(BaseCommand):

    def handle(self, *args, **options):
        my_telegram_bot = MyTelegramBot()
        my_telegram_bot.send_message('Hello!')
