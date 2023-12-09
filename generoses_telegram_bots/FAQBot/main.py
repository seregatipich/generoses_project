from asyncio import run
from logging import basicConfig, INFO
from sys import stdout
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from dotenv import load_dotenv

from keyboards import inline_kb
from handlers import welcome, sub_categories, categories


load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_TOKEN")


dp = Dispatcher()


main_menu_buttons = [
    'Пожертвования',
    'Еще что-то',
    'И еще что-то',
]





async def main() -> None:
    bot = Bot(
        BOT_TOKEN,
        parse_mode=ParseMode.HTML
    )
    dp.include_routers(categories.rt, sub_categories.rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    basicConfig(
        level=INFO,
        stream=stdout
    )
    run(main())
