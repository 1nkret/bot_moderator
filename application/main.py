from urlextract import URLExtract

from aiogram import types, F
from aiogram.filters import Command

from application.database.db import db
from application.finder_urls import url_is_find
from application.bot import dp, bot
from application.info import post_info

url_extractor = URLExtract()


@dp.message(F.text, Command("start"))
async def start(message: types.Message) -> None:
    """
    Command /start for starting the bot
    :param message: message info from telegram chat
    :return: None
    """
    await message.answer("Hello there!")


@dp.message(F.text, Command("info"))
async def info(message: types.Message) -> None:
    """
    Command /info for getting information about this server
    :param message: message info from telegram chat
    :return: None
    """
    await post_info(message)


@dp.message()
async def check_message(message: types.Message):
    """
    Function for check every message in chat
    :param message: message info from telegram chat
    :return: None
    """
    # if message.chat.type != "private":
    if message.chat.type != "private" and message.from_user.id not in [
        el.user.id for el in await bot.get_chat_administrators(message.chat.id)
    ]:
        # Check for URL in message
        if url_extractor.find_urls(message.text):
            await url_is_find(message)


async def main():
    db.create_table()
    await dp.start_polling(bot)


if __name__ == "__main__":
    # asyncio.run(main())
    ...
