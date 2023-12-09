from asyncio import run
from logging import basicConfig, INFO
from sys import stdout
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.methods.answer_inline_query import AnswerInlineQuery
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv

from keyboards import inline_kb


load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_TOKEN")


dp = Dispatcher()


main_menu_buttons = [
    'Пожертвования',
    'Еще что-то',
    'И еще что-то',
]


@dp.message(CommandStart())
async def welcome(message: Message) -> None:
    await message.answer(
        f"Привет! Это бот, который поможет вам разобраться в проблеме с GENEROSES. Чтобы начать, выберете пункт меню, который вам нужен",
        reply_markup=inline_kb(main_menu_buttons, 2)
    )


@dp.callback_query(lambda c: c.data == 'btn0')
async def handle_button_one(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1")


@dp.callback_query(lambda c: c.data == 'btn1')
async def handle_button_two(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2")


@dp.callback_query(lambda c: c.data == 'btn2')
async def handle_button_three(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN3")


async def main() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    basicConfig(level=INFO, stream=stdout)
    run(main())
