import config
import logging

from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = config.config['BOT_TOKEN']

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    print(message)
    await message.reply('Hi!')

@dp.message_handler(content_types=types.ContentType.TEXT)
async def add_idea(message: types.Message):
    print(message)
    await message.reply('Your idea was added')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)