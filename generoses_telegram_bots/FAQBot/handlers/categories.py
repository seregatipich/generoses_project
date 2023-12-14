from aiogram import Router
from aiogram.types import CallbackQuery

from utils.keyboards import inline_kb
from config.data_handlers import format_subsection_qa_pairs_json
from utils.bot import bot


rt = Router()


@rt.callback_query(lambda c: c.data == 'Пожертвования')
async def handle_button_one(callback_query: CallbackQuery) -> None:
    await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=inline_kb(
            list(format_subsection_qa_pairs_json('Пожертвования').keys()),
            2
        )
    )
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Как')
async def handle_button_two(callback_query: CallbackQuery) -> None:
    await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=inline_kb(
            list(format_subsection_qa_pairs_json('Как это работает?').keys()),
            2
        )
    )
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Участие')
async def handle_button_three(callback_query: CallbackQuery) -> None:
    await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=inline_kb(list(format_subsection_qa_pairs_json('Участие и Волонтерство').keys()),
                               2
                               )
    )
    await callback_query.answer()
