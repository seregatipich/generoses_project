from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_inline_kb_main(main_menu_buttons: list) -> InlineKeyboardBuilder:

    builder = InlineKeyboardBuilder()
    for i in range(0, len(main_menu_buttons)):
        builder.button(text=f"{main_menu_buttons[i]}", callback_data=f"btn{i}")
        builder.adjust(2, 2)
        
    return builder.as_markup()

