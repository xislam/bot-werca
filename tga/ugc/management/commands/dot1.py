
from aiogram.utils import executor
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from django.utils import asyncio

from ugc.models import Profile, Message

bot = Bot(token='1098748898:AAGSa4WZlOLHb-ikuFUQ_rHCfamx8yVLSIQ')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Задайте свой вапрос')


@dp.message_handler()
async def process_start_command(message: types.Message):
    if message.text:
        await fm(message)
        await message.reply(
            text=f'Хорошо с вами свяжутся'
        )


@sync_to_async
def fm(message):
    chat_id = message.from_user.id
    text = message.text

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': message.from_user.username,
        }
    )
    m = Message(
        profile=p,
        text=text,
    )
    m.save()


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        executor.start_polling(dp)
