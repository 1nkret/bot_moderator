import asyncio
from urlextract import URLExtract

from aiogram import Bot, Dispatcher
from aiogram import types, F
from aiogram.filters import Command

from os import getenv

from dotenv import load_dotenv

# load token
load_dotenv()
token = getenv("TOKEN")

# init bot
bot = Bot(token)
dp = Dispatcher()

# extractor url`s
url_extractor = URLExtract()


@dp.message(F.text, Command("start"))
async def start(message: types.Message):
    await message.answer("Hello there!")


@dp.message()
async def echo(message: types.Message):
    if message.chat.type == "supergroup":
        if url_extractor.find_urls(message.text):
            await message.delete()
            await message.answer(
                f"{message.from_user.first_name} ({message.from_user.id}) have X warns. Reason: Y")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
