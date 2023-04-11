"""
Задача № 49.
+ 1. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
номер телефона - данные, которые должны находиться в файле.
    1) Программа должна выводить данные.
    2) Программа должна сохранять данные в текстовом файле.
    3) Пользователь может ввести одну из характеристик для поиска определенной записи (например, имя или фамилию).
    4) Использование функций. Ваша программа не должна быть линейной.

+ 2. Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или
фамилию, и Вы должны реализовать функционал для изменения и удаления данных

3. Настроить взаимодействие со справочником через чат телеграмма.
"""

import json
import os
import pathlib
import re


def add_contact(file_name: str) -> None:
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
    phone_number = phone_number_is_correct()
    new_contact_dict = {'id': contact_id, 'name': name, 'surname': surname, 'patronymic': patronymic,
                        'phone_number': phone_number}
    file.append(new_contact_dict)
    return file


def delete_contact(file_name: str) -> int:
    file = open_file(file_name)
    if file:
        print('\n<!-- Найдите контакт, который необходимо удалить --!>\n')
        if searching_contact(file_name):
            contact_id_delete = input('Введите номер контакта, который необходимо удалить: ')
            try:
                contact_delete = next(x for x in file if contact_id_delete in str(x['id']))
                file.remove(contact_delete)
                save_file(file, file_name)
                print('\n<!-- Контакт успешно удален --!>\n')
            except StopIteration:
                print('\n<!-- Вы ввели некорректные данные --!>\n')
        else:
            delete_contact(file_name)
    return 0


def update_contact(file_name: str) -> int:
    file = open_file(file_name)
    if file:
        print('\n<!-- Найдите контакт, который необходимо изменить --!>\n')
        if searching_contact(file_name):
            contact_id_update = input('Введите номер контакта, который необходимо изменить: ')
            try:
                contact_update = next(x for x in file if contact_id_update in str(x['id']))
                contact_update_index = file.index(contact_update)
                update_menu(file, contact_update_index, file_name)
            except StopIteration:
                print('\n<!-- Вы ввели некорректные данные --!>\n')
        else:
            update_contact(file_name)
    return 0


def update_fileds(file_list: list, contact_index: int, file_name: str) -> int:
    print('\n<!-- Выберите действие --!>\n')
    update_choice = int(input())
    file_for_update = file_list
    if update_choice == 1:
        name = input('Введите имя: ').capitalize()
        file_for_update[contact_index]['name'] = name
    elif update_choice == 2:
        surname = input('Введите фамилию: ').capitalize()
        file_for_update[contact_index]['surname'] = surname
    elif update_choice == 3:
        patronymic = input('Введите отчество: ').capitalize()
        file_for_update[contact_index]['patronymic'] = patronymic
    elif update_choice == 4:
        phone_number = phone_number_is_correct()
        file_for_update[contact_index]['phone_number'] = phone_number
    elif update_choice == 5:
        save_file(file_for_update, file_name)
        print('\n<!-- Изменения сохранены --!>\n')
    else:
        return 0
    return 1


def update_menu(file_list: list, contact_index: int, file_name: str) -> int:
    data_update = {1: 'Изменить имя',
                   2: 'Изменить фамилию',
                   3: 'Изменить отчество',
                   4: 'Изменить номер',
                   5: 'Сохранить изменения',
                   6: 'Закрыть меню'}
    print('-' * 10)
    print('\n'.join(f'{k}: {v}' for k, v in data_update.items()))
    print('-' * 10)
    if not update_fileds(file_list, contact_index, file_name):
        return 0
    update_menu(file_list, contact_index, file_name)


def phone_number_is_correct() -> str:
    phone_number = input('Введите номер телефона (с 8 или +7): ')
    if len(phone_number) < 13 and \
            [m.group() for m in re.finditer(r"((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", phone_number)]:
        return phone_number
    else:
        print('Некорректный номер телефона! Попробуйте еще раз')
        phone_number_is_correct()


def create_file(file_name: str) -> list:
    with open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'w', encoding='UTF-8'):
        pass
    return list()


def open_file(file_name: str) -> list or int:
    with open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'r', encoding='UTF-8') as contacts_list:
        try:
            file = json.load(contacts_list)
            return file
        except json.decoder.JSONDecodeError:
            print('\n<!-- Справочник пуст --!>\n')
            return 0


def save_file(file: list, file_name: str) -> None:
    with open(os.path.join(os.path.dirname(__file__), f'{file_name}.txt'), 'w', encoding='UTF-8') as contacts_list:
        json.dump(file, contacts_list, indent=2, ensure_ascii=False)


def searching_contact(file_name) -> int:
    file = open_file(file_name)
    if file:
        search = input(f'Введите запрос (пустая строка для вывода всего справочника): ').capitalize()
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


def file_is_exists(file_name: str) -> str or list:
    if not pathlib.Path(f'{file_name}.txt').exists():
        print('<!-- Такого файла не существует! -->')
        print('<!-- Создаем -->')
        create_file(file_name)
        return list()
    return file_name


def user_choice(file_name: str) -> int:
    print('<!-- Что делаем? --!>')
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
        print('\n<!-- Завершена работа со справочником --!>')
        return 0
    return 1


def menu_print(file_name: str) -> int:
    data = {1: 'Добавить контакт',
            2: 'Поиск по справочнику',
            3: 'Изменить контакт',
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
