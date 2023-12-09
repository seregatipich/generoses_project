from aiogram import types, Router

rt = Router()


@rt.callback_query(lambda c: c.data == 'btn0')
async def handle_button_one(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN0")

@rt.callback_query(lambda c: c.data == 'btn0_sub0')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN0_0")

@rt.callback_query(lambda c: c.data == 'btn0_sub1')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN0_1")

@rt.callback_query(lambda c: c.data == 'btn0_sub2')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN0_2")


@rt.callback_query(lambda c: c.data == 'btn1')
async def handle_button_one(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1")

@rt.callback_query(lambda c: c.data == 'btn1_sub0')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1_0")

@rt.callback_query(lambda c: c.data == 'btn1_sub1')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1_1")

@rt.callback_query(lambda c: c.data == 'btn1_sub2')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN1_2")


@rt.callback_query(lambda c: c.data == 'btn2')
async def handle_button_one(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2")

@rt.callback_query(lambda c: c.data == 'btn2_sub0')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2_0")

@rt.callback_query(lambda c: c.data == 'btn2_sub1')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2_1")

@rt.callback_query(lambda c: c.data == 'btn2_sub2')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(text="BTN2_2")