from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()


async def cmd_test1(message: types.Message):
    await message.reply('Test 1')


async def cmd_test2(message: types.Message):
    await message.reply('Test 2')



async def main():
    dp.message.register(cmd_test2, F.text,  Command('test2'))
    dp.message.register(cmd_test1, Command('test1'))
    await dp.start_polling(bot)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())