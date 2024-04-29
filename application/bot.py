from aiogram import Bot, Dispatcher

from os import getenv
from dotenv import load_dotenv

# load token
load_dotenv()
token = getenv("TOKEN")

# init bot
bot = Bot(token)
dp = Dispatcher()
