"""
*****(4)Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса, сформированную из
отсортированных в лексикографическом порядке параметров.
Пример:
Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
challenge=17&course=python&lesson=2
"""

# in_dict = {'course': 'python', 'lesson': 2, 'challenge': 17}
# sort_in_dict = sorted(in_dict.items(), key=lambda x: x[0])
# print(sort_in_dict)
# print(sort_in_dict[0][1])
# for i in sort_in_dict:
#     text = '&'.join('='.join(str(_)) for _ in i)
# print(text)