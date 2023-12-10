from aiogram import Router, types

from config.data_handlers import format_subsection_qa_pairs_json
from keyboards import inline_kb


rt = Router()


# Начало хэндлеров для категории "Пожертвования"
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
# Конец хэндлеров для категории "Пожертвования"


# Начало хэндлеров для категории "Как это работает?"
@rt.callback_query(lambda c: c.data == 'Общий')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Как это работает?')['Общий Процесс и Механизмы']))
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Руководства')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Как это работает?')['Руководства и Инструкции']))
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Политика')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Как это работает?')['Политика и Принципы']))
    await callback_query.answer()
# Конец хэндлеров для категории "Как это работает?"


# Начало хэндлеров для категории "Участие и Волонтерство"
@rt.callback_query(lambda c: c.data == 'Способы')
async def handle_button_one_sub0(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Участие и Волонтерство')['Способы Участия']))
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Преимущества')
async def handle_button_one_sub1(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Участие и Волонтерство')['Преимущества и Возможности']))
    await callback_query.answer()


@rt.callback_query(lambda c: c.data == 'Поддержка')
async def handle_button_one_sub2(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer('\n\n'.join(format_subsection_qa_pairs_json('Участие и Волонтерство')['Поддержка и Ресурсы']))
    await callback_query.answer()
# Конец хэндлеров для категории "Участие и Волонтерство"