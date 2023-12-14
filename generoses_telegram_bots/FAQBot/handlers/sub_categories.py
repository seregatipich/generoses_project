from aiogram import Router
from aiogram.types import CallbackQuery

from config.constants import main_menu_buttons, FAILURE_MESSAGE, CATEGORIES
from config.data_handlers import format_subsection_qa_pairs_json, manage_user_clicks
from utils.bot import bot
from utils.keyboards import inline_kb


rt = Router()


async def choose_and_send_message(callback_query: CallbackQuery) -> None:
    """
    Process a user's callback query and send an appropriate message response.

    This function first manages the user's click interaction through the
    'manage_user_clicks' function. If the processing result is False,
    it sends a general help message with a main menu. If True, it sends a
    predefined failure message. The function ends by acknowledging the
    callback query.

    Args:
        callback_query (CallbackQuery): The callback query received from the user interaction.

    Returns:
        None
    """
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


# Начало хэндлеров для категории "Пожертвования"
@rt.callback_query(lambda c: c.data == 'Управление')
async def handle_button_one_sub0(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[0]
    sub_category = CATEGORIES[category][0]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' +
        '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )
    await choose_and_send_message(callback_query)


@rt.callback_query(lambda c: c.data == 'Информация')
async def handle_button_one_sub1(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[0]
    sub_category = CATEGORIES[category][1]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' +
        '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    await choose_and_send_message(callback_query)


@rt.callback_query(lambda c: c.data == 'Технические')
async def handle_button_one_sub2(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[0]
    sub_category = CATEGORIES[category][2]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' +
        '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    await choose_and_send_message(callback_query)
# Конец хэндлеров для категории "Пожертвования"


# Начало хэндлеров для категории "Как это работает?"
@rt.callback_query(lambda c: c.data == 'Общий')
async def handle_button_one_sub0(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[1]
    sub_category = CATEGORIES[category][0]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    await choose_and_send_message(callback_query)


@rt.callback_query(lambda c: c.data == 'Руководства')
async def handle_button_one_sub1(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[1]
    sub_category = CATEGORIES[category][1]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    await choose_and_send_message(callback_query)


@rt.callback_query(lambda c: c.data == 'Политика')
async def handle_button_one_sub2(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[1]
    sub_category = CATEGORIES[category][2]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    await choose_and_send_message(callback_query)
# Конец хэндлеров для категории "Как это работает?"


# Начало хэндлеров для категории "Участие и Волонтерство"
@rt.callback_query(lambda c: c.data == 'Способы')
async def handle_button_one_sub0(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[2]
    sub_category = CATEGORIES[category][0]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    await choose_and_send_message(callback_query)


@rt.callback_query(lambda c: c.data == 'Преимущества')
async def handle_button_one_sub1(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[2]
    sub_category = CATEGORIES[category][1]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    await choose_and_send_message(callback_query)


@rt.callback_query(lambda c: c.data == 'Поддержка')
async def handle_button_one_sub2(callback_query: CallbackQuery) -> None:
    category = list(CATEGORIES.keys())[2]
    sub_category = CATEGORIES[category][2]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f'<b>{sub_category}</b>\n\n' + '\n\n'.join(
            format_subsection_qa_pairs_json(category)[sub_category]
        )
    )

    await choose_and_send_message(callback_query)
# Конец хэндлеров для категории "Участие и Волонтерство"
