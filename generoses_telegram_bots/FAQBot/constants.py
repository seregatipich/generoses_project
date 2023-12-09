main_menu_buttons = {
    'Пожертвования': [
        "Управление пожертвованиями",
        "Информация о пожертвованиях и благотворительных проектах",
        "Технические вопросы и проблемы"
    ],

    'Как это работает?': [],
    'Участие и волонтерство': [],
}


def format_qa_pairs_dict(data, section_key):
    """
    Формирует словарь, где ключ - это название раздела, а значение - список строк с вопросами и ответами.

    :param data: словарь с данными
    :param section_key: ключ для выбора соответствующего раздела
    :return: словарь с ключом, указывающим на раздел, и списком отформатированных строк вопрос-ответ
    """
    formatted_pairs = []
    for section in data:
        if section_key in section:
            for qa in section[section_key]:
                question = qa["question"]
                answer = qa["answer"]
                formatted_pair = f"Вопрос: {question}\nОтвет: {answer}"
                formatted_pairs.append(formatted_pair)

    return {section_key: formatted_pairs}
