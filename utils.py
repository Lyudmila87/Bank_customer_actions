
def filter_names_to_delete(names: list) -> list[str]:
    """функция для фильтрации списка имен, записи с которыми необходимо удалить из таблицы"""

    list_of_len_name = [len(name) for name in names]
    return [name for name in names if len(name) == round(sum(list_of_len_name) / len(list_of_len_name))]
