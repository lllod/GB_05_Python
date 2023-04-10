"""
Задача № 49.
1. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
    1) Программа должна выводить данные.
    2) Программа должна сохранять данные в текстовом файле.
    3) Пользователь может ввести одну из характеристик для поиска определенной записи (например, имя или фамилию).
    4) Использование функций. Ваша программа не должна быть линейной.

2. Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или
фамилию, и Вы должны реализовать функционал для изменения и удаления данных

3. Настроить взаимодействие со справочником через чат телеграмма.
"""

import json
import os
import pathlib


# with open('json_test.json', 'w', encoding='UTF-8') as fp:
#     json.dump(a, fp, indent=2, ensure_ascii=False)
#
# with open('json_test.json', 'r', encoding='UTF-8') as fp1:
#     file = json.load(fp1)

# print(file[-1])

# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# patronymic = input('Введите отчество: ')
# phone_number = input('Введите номер телефона: ')
#
# a.append({'id': len(file) + 1,
#           'contact': {'name': name, 'surname': surname, 'patronymic': patronymic, 'phone_number': phone_number}})
#
# print(file[-1])
# print(a)

# search = input('Введите запрос: ')
# search_list = ['name', 'surname', 'patronymic', 'phone_number']
# print(list(filter(lambda el: search in el['name'] or search in el['surname'] or search in
#                              el['patronymic'] or search in el['phone_number'], a)))

# file = open('json_test.json', 'w+', encoding='UTF-8')
# json.dump(a, file, indent=2, ensure_ascii=False)
# print(len(file.read()))
#


def add_contact(file_name='seminar8'):
    if not pathlib.Path(f'{file_name}.txt').exists():
        create_file(file_name)
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(f'{file_name}.txt', 'a+', encoding='UTF-8') as contacts_list:
        file = json.load(contacts_list)
    new_contact_dict = str({'id': len(file) + 1, 'name': name, 'surname': surname, 'patronymic': patronymic,
                            'phone_number': phone_number})
    contacts_list.write(new_contact_dict)


def create_file(file_name: str):
    with open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'w', encoding='UTF-8'):
        pass
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')


def searching_contact(file_name='seminar8'):
    file = open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'r', encoding='URF-8')
    search = input('Введите запрос: ')
    print_contact(list(filter(lambda el: search in el['name'] or search in el['surname'] or search in
                                  el['patronymic'] or search in el['phone_number'], file)))


def print_contact(cotacts_list: list):
    for i in cotacts_list:
        print('\n'.join(f'{k}: {v}' for k, v in i.items() if k != 'id'), end='\n\n')


if __name__ == '__main__':
    # a = [
    #     {
    #         'id': 1,
    #         'name': 'Вася',
    #         'surname': 'Пупкин',
    #         'patronymic': 'Всеволодович',
    #         'phone_number': '+78512666666'
    #     },
    #     {
    #         'id': 2,
    #         'name': 'Слава',
    #         'surname': 'Пупкин',
    #         'patronymic': 'Всеволодович',
    #         'phone_number': '+123'
    #     }
    # ]
    add_contact()
    searching_contact()