import os
from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User
from core.services import TelegramBotSender


load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        telegram_bot_sender = TelegramBotSender()
        chat_id = User.objects.filter(email=os.getenv('CSU_EMAIL')).first().user_id_telegram
        telegram_bot_sender.send_message(chat_id, 'Hello!')
