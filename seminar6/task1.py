"""
Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""


def arithmetic_progression() -> list:
    print('Введите первый элемент:', end=' ')
    start_el = is_digit()
    print('Введите разность:', end=' ')
    step = is_digit()
    print('Введите количество элементов:', end=' ')
    el_count = is_digit()
    return [i for i in range(start_el, start_el + el_count * step, step)]


def is_digit() -> int:
    while True:
        num = input()
        try:
            int(num)
            return int(num)
        except ValueError:
            print('Необходимо ввести целое число!')


if __name__ == '__main__':
    arithmetic_progression_list = arithmetic_progression()
    print(*arithmetic_progression_list)
