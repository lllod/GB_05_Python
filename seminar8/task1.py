"""
Задача № 49.
+ 1. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
номер телефона - данные, которые должны находиться в файле.
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


def add_contact(file_name) -> None:
    try:
        file = open_file(file_name)
        contact_id = file[-1]['id'] + 1
    except json.decoder.JSONDecodeError:
        file = create_file(file_name)
        contact_id = 1
    new_contact_info(file, contact_id)
    save_file(file, file_name)
    print('\n<!-- Контакт успешно добавлен --!>\n')


def new_contact_info(file: list, contact_id: int) -> list:
    name = input('Введите имя: ').capitalize()
    surname = input('Введите фамилию: ').capitalize()
    patronymic = input('Введите отчество: ').capitalize()
    phone_number = input('Введите номер телефона: ')
    new_contact_dict = {'id': contact_id, 'name': name, 'surname': surname, 'patronymic': patronymic,
                        'phone_number': phone_number}
    file.append(new_contact_dict)
    return file


def delete_contact(file_name):
    print('\n<!-- Найдите контакт, который необходимо удалить --!>\n')
    if searching_contact(file_name):
        contact_id_delete = input('Введите номер контакта, который необходимо удалить: ')
        file = open_file(file_name)
        try:
            contact_delete = next(x for x in file if contact_id_delete in str(x['id']))
            file.remove(contact_delete)
            save_file(file, file_name)
            print('\n<!-- Контакт успешно удален --!>\n')
        except StopIteration:
            print('\n<!-- Вы ввели некорректные данные --!>\n')
    else:
        delete_contact(file_name)


def update_contact(file_name):
    print('\n<!-- Найдите контакт, который необходимо изменить --!>\n')
    if searching_contact(file_name):
        contact_id_update = input('Введите номер контакта, который необходимо изменить: ')
        file = open_file(file_name)
        try:
            contact_update = next(x for x in file if contact_id_update in str(x['id']))
            print(contact_update)
        except StopIteration:
            print('\n<!-- Вы ввели некорректные данные --!>\n')
    else:
        update_contact(file_name)


def create_file(file_name: str) -> list:
    with open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'w', encoding='UTF-8'):
        pass
    return list()


def open_file(file_name: str) -> list:
    with open(f'{file_name}.txt', 'r', encoding='UTF-8') as contacts_list:
        file = json.load(contacts_list)
    return file


def save_file(file: list, file_name: str) -> None:
    with open(f'{file_name}.txt', 'w', encoding='UTF-8') as contacts_list:
        json.dump(file, contacts_list, indent=2, ensure_ascii=False)


def searching_contact(file_name) -> int:
    with open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'r', encoding='UTF-8') as contact_list:
        try:
            file = json.load(contact_list)
        except json.decoder.JSONDecodeError:
            print('\n<!-- Справочник пуст --!>\n')
            return 0
        search = input(f'Введите запрос (пустая строка для вывода всего справочника): \n').capitalize()

        found_contacts = (list(filter(
            lambda el: search in el['name'] or search in el['surname'] or search in el['patronymic'] or search in el[
                'phone_number'],
            file)))
        if found_contacts:
            print_contact(found_contacts)
            return 1
        else:
            print('\n<!-- Найти контакт не удалось, попробуйте еще раз --!>\n')
            return 0


def print_contact(contacts_list: list) -> None:
    human_key = {'id': 'Номер записи',
                 'name': 'Имя',
                 'surname': 'Фамилия',
                 'patronymic': 'Отчество',
                 'phone_number': 'Номер телефона'}
    for i in contacts_list:
        print(f"\n\tКонтакт № {i['id']}")
        print('\n'.join(f'{human_key[k]}: {v}' for k, v in i.items() if k != 'id'), end='\n')


def file_is_exists(file_name: str):
    if not pathlib.Path(f'{file_name}.txt').exists():
        print('<!-- Такого файла не существует! -->')
        print('<!-- Создаем -->')
        create_file(file_name)
        return list()
    return file_name


def user_choice(file_name: str) -> int:
    print('Что делаем?')
    choice = int(input())
    if choice == 1:
        add_contact(file_name)
    elif choice == 2:
        searching_contact(file_name)
    elif choice == 3:
        update_contact(file_name)
    elif choice == 4:
        delete_contact(file_name)
    else:
        print('<!-- Работа со справочником завершается --!>')
        return 0
    return 1


def menu_print(file_name: str) -> int:
    data = {1: 'Добавить контакт',
            2: 'Поиск по справочнику',
            3: 'Обновить контакт',
            4: 'Удалить контакт',
            5: 'Закончить работу со справочником'}
    print('-' * 10)
    print('\n'.join(f'{k}: {v}' for k, v in data.items()))
    print('-' * 10)
    if not user_choice(file_name):
        return 0
    menu_print(file_name)


def main_menu(file_name: str) -> None:
    file_is_exists(file_name)
    menu_print(file_name)


if __name__ == '__main__':
    name_file = input('Введите название файла на латинице: ')
    main_menu(name_file)
