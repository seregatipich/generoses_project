from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_inline_kb_main(buttons_names: list) -> InlineKeyboardBuilder:

    builder = InlineKeyboardBuilder()
    for i in range(0, len(buttons_names)):
        builder.button(text=f"{buttons_names[i]}", callback_data=f"btn{i}")
        builder.adjust(2, 2) # ПОФИКСИТЬ - СДЕЛАТЬ АРГУМЕНТОМ ФУНКЦИИ
        
    return builder.as_markup()

