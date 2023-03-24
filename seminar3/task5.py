"""
*****(4)Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса, сформированную из
отсортированных в лексикографическом порядке параметров.
Пример:
Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
challenge=17&course=python&lesson=2
"""


def dict_to_query(in_dict: dict) -> str:
    sort_in = sorted(in_dict.items())
    query = '&'.join([f'{key}={value}' for key, value in sort_in])
    return query


if __name__ == '__main__':
    in_dict = {'course': 'python', 'lesson': 2, 'challenge': 17}
    print(dict_to_query(in_dict))
