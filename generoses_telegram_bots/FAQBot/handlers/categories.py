from aiogram import Router
from aiogram.types import CallbackQuery


rt = Router()


@rt.callback_query(lambda c: c.data == 'btn0')
async def handle_button_one(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn1')
async def handle_button_two(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn2')
async def handle_button_three(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN3")
    await callback_query.answer()