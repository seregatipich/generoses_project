import json

main_menu_buttons = [
    'Пожертвования',
    'Как это работает?',
    'Участие и волонтерство'
]


def format_subsection_qa_pairs_json(main_section):
    """
    Формирует словарь, где каждый ключ - это подраздел внутри основного раздела, а значение - список строк с вопросами и ответами.

    :param data: JSON документ
    :param main_section: основной раздел для поиска подразделов
    :return: словарь, где ключи - это подразделы, и списки отформатированных строк вопрос-ответ в качестве значений
    """

    JSON_PATH = 'generoses_telegram_bots/FAQBot/questions-answers.json'

    with open(JSON_PATH, 'r', encoding='utf-8') as file:
        json_data_from_file = json.load(file)

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

# print(format_subsection_qa_pairs_json('Пожертвования'))
# print(list(format_subsection_qa_pairs_json('Пожертвования').keys()))
