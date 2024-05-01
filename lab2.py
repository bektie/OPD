
import asyncio
import logging
import sys
import random
from os import getenv

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6739525703:AAH6hb5LrfpkERjisAX8DU96CO4TSiwDhok"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

def randomize():
    a = random.randint(1,2)
    if a == 1:
        idx = 'AgACAgIAAxkBAAMOZgEJkaFOmN815PfhpZD-_lki2GgAAnTWMRtimQhI-Z7xwWRJMIQBAAMCAAN5AAM0BA'
    else:
        idx = 'AgACAgIAAxkBAAMQZgEKapIB64GoaivDHMU6RSgULOMAAnrWMRtimQhICceBt9KI1PkBAAMCAAN5AAM0BA'
    return idx

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer_photo(photo = randomize())






@dp.message()
async def echo_handler(message: types.Message) -> None:

    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())