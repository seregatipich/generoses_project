from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def inline_kb(buttons_names: list, keyboard_size: int) -> InlineKeyboardMarkup:
    """
    Creates an inline keyboard with buttons using the provided button names and keyboard size.

    The function constructs an inline keyboard where each button is created based on the items
    in the `buttons_names` list. The `keyboard_size` parameter determines the layout of the
    keyboard, specifying how many buttons are placed in each row.

    Args:
        buttons_names (list): A list of strings representing the names of the buttons to be included
                              in the inline keyboard. Each string in the list becomes the text of
                              a button, and its first word (separated by space) is used as the
                              callback data for the button.
        keyboard_size (int): An integer specifying the number of buttons in each row of the
                             inline keyboard.

    Returns:
        InlineKeyboardMarkup: An object representing the inline keyboard layout, ready to be
                              used in a Telegram bot interface.
    """
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

