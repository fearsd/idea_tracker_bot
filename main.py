import logging
import os

from aiogram import Bot, Dispatcher, executor, types

import config
import models
from handlers import register_user
from models import get_db, get_engine

try:
    BOT_TOKEN = config.config['BOT_TOKEN']
except BaseException:
    BOT_TOKEN = os.environ['BOT_TOKEN']

models.Base.metadata.create_all(get_engine())

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    print(message)
    user = register_user(data={
        'telegram_id': message['from']['id']
    }, db=next(get_db()))
    print(user)
    await message.reply('Hi!')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def add_idea(message: types.Message):
    print(message)
    await message.reply('Your idea was added')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
