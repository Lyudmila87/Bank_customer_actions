
def filter_names_to_delete(names: list) -> list:
    """функция для фильтрации списка имен, записи с которыми необходимо удалить из таблицы"""

    list_of_len_name = [len(name) for name in names]
    average = sum(list_of_len_name) / len(list_of_len_name)
    list_to_delete = []
    for name in names:
        if len(name) == int(average) or len(name) == round(average):
            list_to_delete.append(name)
    return list_to_delete
