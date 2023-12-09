from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import inline_kb
from constants import main_menu_buttons


rt = Router()


@rt.message(CommandStart())
async def welcome(message: Message) -> None:
    await message.answer(
        f"Привет! Это бот, который поможет вам разобраться в проблеме с GENEROSES. Чтобы начать, выберете пункт меню, который вам нужен",
        reply_markup=inline_kb(main_menu_buttons, 2)
    )
