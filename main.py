"""Module starts the telegram bot"""
import logging
import os

from aiogram import Bot, Dispatcher, executor, types

import config
from handlers import register_user
from models import get_db, get_engine, Base

try:
    BOT_TOKEN = config.config['BOT_TOKEN']
except KeyError:
    BOT_TOKEN = os.environ['BOT_TOKEN']

Base.metadata.create_all(get_engine())

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """Message handler on start command."""
    user_data = {
        'telegram_id': message['from']['id']
    }
    register_user(user_data=user_data, db=next(get_db()))
    await message.reply('Hi!')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def add_idea(message: types.Message):
    """Message handler on text."""
    await message.reply('Your idea was added')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
