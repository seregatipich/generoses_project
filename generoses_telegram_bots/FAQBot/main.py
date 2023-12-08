from asyncio import run 
from logging import basicConfig, INFO
from sys import stdout
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.methods.answer_inline_query import AnswerInlineQuery
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_TOKEN")

dp = Dispatcher()
router = Router()


CATEGORIES = {"btn1":[], "bt2":[], "btn3":[]}


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    for index in range(1, 4):
        builder.button(text=f"btn{index}", callback_data=f"btn{index}")
        builder.adjust(2, 2)
    await message.answer(f"Привет! Это бот, который поможет вам разобраться в проблеме с GENEROSES. Чтобы начать, нажмите /start", reply_markup=builder.as_markup())


@dp.callback_query() #(lambda c: c.data == 'btn1')
async def handle_help(callback_query: types.CallbackQuery) -> None:
    if callback_query.data == "btn1":
        await callback_query.message.answer(text="BTN1")
    elif callback_query.data == "btn2":
        await callback_query.message.answer(text="BTN2")
    elif callback_query.data == "btn3":
        await callback_query.message.answer(text="BTN3")
    await callback_query.answer()
    

async def main() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    basicConfig(level=INFO, stream=stdout)
    run(main())
