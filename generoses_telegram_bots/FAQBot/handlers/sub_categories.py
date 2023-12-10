from aiogram import Router, types

from config.data_handlers import format_subsection_qa_pairs_json
from keyboards import inline_kb


rt = Router()


@rt.callback_query(lambda c: c.data == 'Управление')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Пожертвования')['Управление пожертвованиями']))
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Информация')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Пожертвования')['Информация о пожертвованиях и благотворительных проектах']))
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Технические')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Пожертвования')['Технические вопросы и проблемы']))
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
