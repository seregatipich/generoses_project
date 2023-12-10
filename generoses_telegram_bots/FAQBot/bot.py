from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_TOKEN")


dp = Dispatcher()
bot = Bot(
    BOT_TOKEN,
    parse_mode=ParseMode.HTML
)
