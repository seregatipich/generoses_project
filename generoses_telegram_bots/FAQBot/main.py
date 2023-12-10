from asyncio import run
from logging import INFO, basicConfig
from os import getenv
from sys import stdout

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers import welcome, sub_categories, categories


load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_TOKEN")


dp = Dispatcher()
bot = Bot(
    BOT_TOKEN,
    parse_mode=ParseMode.HTML
)


async def main() -> None:
    dp.include_routers(categories.rt, sub_categories.rt, welcome.rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    basicConfig(
        level=INFO,
        stream=stdout
    )
    run(main())
