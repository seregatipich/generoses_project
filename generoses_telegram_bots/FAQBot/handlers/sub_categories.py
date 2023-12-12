from aiogram import Router, types

from config.constants import main_menu_buttons
from config.data_handlers import format_subsection_qa_pairs_json
from keyboards import inline_kb
from config.db_handlers import *
from bot import bot


rt = Router()


def process_user(user_id) -> bool:
    """
    Processes a user's action from a Telegram bot callback query and manages their click count.

    This function performs a series of operations involving the user's click count:
    1. If the user does not exist in the 'users' table, they are inserted with an initial click count of zero.
    2. The user's click count is incremented by one.
    3. If the user's click count exceeds three, it is reset to zero.

    The user's ID is determined from the callback query received from the Telegram bot interaction.

    :param callback_query: The callback query received from a Telegram user interaction, containing the user's ID.
    :return: Returns True if the user's click count was over three and has been reset; otherwise, returns False.
    """
    
    insert_user_with_zero_clicks(user_id)
    increment_clicks(user_id)

    return reset_clicks_if_over_three(user_id)


async def manage_user_clicks(callback_query: types.CallbackQuery) -> bool:
    """
    Manages click interactions for a user in a Telegram bot session and responds accordingly.

    This function performs the following actions:
    1. Extracts the user ID from the callback query.
    2. Processes the user's click activity using the `process_user` function.
    3. Based on the result of `process_user`, it sends an appropriate response back to the user via the Telegram bot.

    If `process_user` returns True (indicating a specific condition like exceeding a click threshold), a message related to email is sent. Otherwise, a general help message is sent, along with a main menu.

    :param callback_query: The callback query received from a Telegram bot, containing the user's interaction data.
    """
    user_id = callback_query.from_user.id
    processing_result = process_user(user_id)
    
    return processing_result

# Начало хэндлеров для категории "Пожертвования"
@rt.callback_query(lambda c: c.data == 'Управление')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Управление пожертвованиями'
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Пожертвования')[sub_category]))
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Информация')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Информация о пожертвованиях и благотворительных проектах'
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Пожертвования')[sub_category]))
    
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Технические')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Технические вопросы и проблемы'
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Пожертвования')[sub_category]))
    
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()
# Конец хэндлеров для категории "Пожертвования"


# Начало хэндлеров для категории "Как это работает?"
@rt.callback_query(lambda c: c.data == 'Общий')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Общий Процесс и Механизмы'
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Как это работает?')[sub_category]))
    
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Руководства')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Руководства и Инструкции'
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Как это работает?')[sub_category]))
    
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Политика')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Политика и Принципы'
    print(format_subsection_qa_pairs_json('Пожертвования'))
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Как это работает?')[sub_category]))
    
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()
# Конец хэндлеров для категории "Как это работает?"


# Начало хэндлеров для категории "Участие и Волонтерство"
@rt.callback_query(lambda c: c.data == 'Способы')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Способы Участия'
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Участие и Волонтерство')[sub_category]))
    
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Преимущества')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Преимущества и Возможности'
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Участие и Волонтерство')[sub_category]))
    
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Поддержка')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    sub_category = 'Поддержка и Ресурсы'
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(format_subsection_qa_pairs_json('Участие и Волонтерство')[sub_category]))
    
    processing_result = await manage_user_clicks(callback_query)
    if processing_result == False:
        await callback_query.message.answer('Чем я могу помочь?', reply_markup=inline_kb(main_menu_buttons, 2))
    elif processing_result == True:
        await callback_query.message.answer('Электронная почта')
    
    await callback_query.answer()
# Конец хэндлеров для категории "Участие и Волонтерство"
