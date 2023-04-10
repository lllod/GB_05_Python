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
import uuid


def add_contact(file_name='seminar8'):
    if not pathlib.Path(f'{file_name}.txt').exists():
        file = create_file(file_name)
    else:
        file = open_file(file_name)
    new_contact_info(file)
    save_file(file, file_name)


def new_contact_info(file: list):
    contact_id = str(uuid.uuid4())[:8]
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    new_contact_dict = {'id': contact_id, 'name': name, 'surname': surname, 'patronymic': patronymic,
                        'phone_number': phone_number}
    file.append(new_contact_dict)
    return file


def create_file(file_name: str):
    with open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'w', encoding='UTF-8') as new_file:
        pass
    return list()


def open_file(file_name: str):
    with open(f'{file_name}.txt', 'r', encoding='UTF-8') as contacts_list:
        file = json.load(contacts_list)
    return file


def save_file(file: list, file_name: str):
    with open(f'{file_name}.txt', 'w', encoding='UTF-8') as contacts_list:
        json.dump(file, contacts_list, indent=2, ensure_ascii=False)
    print('<!-- Контакт успешно добавлен --!>')


def searching_contact(file_name='seminar8'):
    with open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'r', encoding='UTF-8') as contact_list:
        file = json.load(contact_list)
        search = input('Введите запрос: ').upper()
        print_contact(list(filter(
            lambda el: search in el['name'].upper() or search in el['surname'].upper() or search in el[
                'patronymic'].upper() or search in el['phone_number'].upper(), file)))


def print_contact(contacts_list: list):
    human_key = {'name': 'Имя', 'surname': 'Фамилия', 'patronymic': 'Отчество', 'phone_number': 'Номер телефона'}
    for i in contacts_list:
        print('\n'.join(f'{human_key[k]}: {v}' for k, v in i.items() if k != 'id'), end='\n\n')


def user_choice():
    data = {1: 'Добавить контакт',
            2: 'Поиск по справочнику',
            3: 'Обновить контакт',
            4: 'Удалить контакт',
            5: 'Закончить работу со справочником'}
    print('-' * 10)
    print('\n'.join(f'{k}: {v}' for k, v in data.items()))
    print('-' * 10)
    print('Что делаем?')
    choice = int(input())
    if choice == 1:
        add_contact()
    elif choice == 2:
        searching_contact()
    else:
        print('<!-- Работа со справочником завершается --!>')
        return 0
    user_choice()



if __name__ == '__main__':
    user_choice()
