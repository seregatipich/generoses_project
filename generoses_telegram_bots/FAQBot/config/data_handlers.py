from json import load


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
