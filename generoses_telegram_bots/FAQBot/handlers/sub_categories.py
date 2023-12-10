from aiogram import types, Router

from constants import format_subsection_qa_pairs_json
from main import bot
from keyboards import inline_kb


rt = Router()


@rt.callback_query(lambda c: c.data == 'Управление')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    # await bot.edit_message_reply_markup(
    #     chat_id=callback_query.from_user.id,
    #     message_id=callback_query.message.message_id,
    #     reply_markup=inline_kb(
    #         format_subsection_qa_pairs_json(
    #             'Пожертвования'
    #         )[
    #             'Управление пожертвованиями'
    #         ],
    #         2
    #     )
    # )
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Информация')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN0_1")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Технические')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN0_2")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn1_sub0')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1_0")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn1_sub1')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1_1")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn1_sub2')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1_2")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn2')
async def handle_button_one(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn2_sub0')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2_0")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn2_sub1')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2_1")
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'btn2_sub2')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2_2")
    await callback_query.answer()
