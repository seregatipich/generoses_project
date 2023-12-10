from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config.constants import main_menu_buttons
from keyboards import inline_kb

rt = Router()


@rt.message(CommandStart())
async def shalom(message: Message) -> None:
    await message.answer(
        f"Привет! Это бот, который поможет вам разобраться в проблеме с GENEROSES. Чтобы начать, выберете пункт меню, который вам нужен",
        reply_markup=inline_kb(main_menu_buttons, 2)
    )
