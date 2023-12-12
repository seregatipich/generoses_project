from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_kb(buttons_names: list, keyboard_size: int) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    for i in range(0, len(buttons_names)):
        data = buttons_names[i].split(maxsplit=1)[0] if buttons_names[i] else ''
        builder.button(
            text=f"{buttons_names[i]}",
            callback_data=f"{data}"
        )
        builder.adjust(
            keyboard_size,
            keyboard_size
        )

    return builder.as_markup()
