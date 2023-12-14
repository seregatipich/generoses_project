from aiogram import Router, types

from config.constants import main_menu_buttons, FAILURE_MESSAGE
from config.data_handlers import format_subsection_qa_pairs_json, manage_user_clicks
from utils.bot import bot
from utils.keyboards import inline_kb


rt = Router()


# Начало хэндлеров для категории "Пожертвования"
@rt.callback_query(lambda c: c.data == 'Управление')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    category = 'Пожертвования'
    sub_category = 'Управление пожертвованиями'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' +
        '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?',
            reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Информация')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    category = 'Пожертвования'
    sub_category = 'Информация о пожертвованиях и благотворительных проектах'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' +
        '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?',
            reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Технические')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    category = 'Пожертвования'
    sub_category = 'Технические вопросы и проблемы'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' +
        '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?',
            reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()
# Конец хэндлеров для категории "Пожертвования"


# Начало хэндлеров для категории "Как это работает?"
@rt.callback_query(lambda c: c.data == 'Общий')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    category = 'Как это работает?'
    sub_category = 'Общий Процесс и Механизмы'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?', reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Руководства')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    category = 'Как это работает?'
    sub_category = 'Руководства и Инструкции'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?',
            reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Политика')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    category = 'Как это работает?'
    sub_category = 'Политика и Принципы'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?',
            reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()
# Конец хэндлеров для категории "Как это работает?"


# Начало хэндлеров для категории "Участие и Волонтерство"
@rt.callback_query(lambda c: c.data == 'Способы')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    category = 'Участие и Волонтерство'
    sub_category = 'Способы Участия'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?',
            reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Преимущества')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    category = 'Участие и Волонтерство'
    sub_category = 'Преимущества и Возможности'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?',
            reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Поддержка')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    category = 'Участие и Волонтерство'
    sub_category = 'Поддержка и Ресурсы'
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer(
            'Чем я могу помочь?',
            reply_markup=inline_kb(
                main_menu_buttons,
                2
            )
        )
    elif processing_result == True:
        await callback_query.message.answer(FAILURE_MESSAGE)

    await callback_query.answer()
# Конец хэндлеров для категории "Участие и Волонтерство"
