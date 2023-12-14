from json import load

from aiogram.types import CallbackQuery

from .db_handlers import (insert_user_with_zero_clicks,
                          increment_clicks,
                          reset_clicks_if_over_three)


def format_subsection_qa_pairs_json(main_section: str) -> dict:
    """
    Reads a JSON file and formats the question-answer pairs for a specified main section.

    This function opens a JSON file defined by the 'JSON_PATH' constant. It then iterates through 
    the data to find and format question-answer pairs related to a specified main section. The 
    function formats these pairs into a readable string format and groups them by their subsections.

    Args:
        main_section (str): The main section in the JSON file for which the question-answer pairs 
                            are to be formatted.

    Returns:
        dict: A dictionary where each key is a subsection under the main section, and each value is a 
              list of formatted question-answer strings corresponding to that subsection.
    """
    from .constants import JSON_PATH

    with open(JSON_PATH, 'r', encoding='utf-8') as file:
        json_data_from_file = load(file)

    formatted_dict = {}
    for item in json_data_from_file:
        if main_section in item:
            for subsections in item[main_section]:
                for subsection, qa_pairs in subsections.items():
                    formatted_pairs = []
                    for pair in qa_pairs:
                        question = pair["question"]
                        answer = pair["answer"]
                        formatted_pair = f"Вопрос: {question}\nОтвет: {answer}"
                        formatted_pairs.append(formatted_pair)
                    formatted_dict[subsection] = formatted_pairs

    return formatted_dict


def process_user(user_id) -> bool:
    """
    Processes a user's action from a Telegram bot callback query, managing their click count.

    This function handles three main operations related to a user's click count in the 'users' table:
    1. Inserts the user with an initial click count of zero if they do not exist in the table.
    2. Increments the user's click count by one.
    3. Resets the user's click count to zero if it exceeds three.

    The function operates based on the user ID derived from the Telegram bot's callback query.

    Args:
        user_id: The unique identifier of the user, extracted from the callback query.

    Returns:
        bool: True if the user's click count was over three and has been reset; False otherwise.
    """
    insert_user_with_zero_clicks(user_id)
    increment_clicks(user_id)

    return reset_clicks_if_over_three(user_id)


async def manage_user_clicks(callback_query: CallbackQuery) -> bool:
    """
    Manages a user's click interactions in a Telegram bot session and sends appropriate responses.

    This asynchronous function executes a sequence of actions based on a user's interaction with a Telegram bot:
    1. It extracts the user ID from the callback query.
    2. The user's click activity is processed using the `process_user` function.
    3. Depending on the result from `process_user`, the function sends a specific response via the Telegram bot.
       - If `process_user` returns True (indicating a condition like exceeding a click threshold), a message related to 
         that condition is sent.
       - Otherwise, a general help message along with a main menu is sent.

    Args:
        callback_query (types.CallbackQuery): The callback query from a Telegram bot containing user interaction data.

    Returns:
        bool: The result from processing the user's click activity.
    """
    user_id = callback_query.from_user.id
    processing_result = process_user(user_id)

    return processing_result
