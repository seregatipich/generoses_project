from asyncio import run 
from logging import basicConfig, INFO
from sys import stdout
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.methods.answer_inline_query import AnswerInlineQuery
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_TOKEN")

dp = Dispatcher()
router = Router()


@dp.message


async def main() -> None:
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    basicConfig(level=INFO, stream=stdout)
    run(main())
