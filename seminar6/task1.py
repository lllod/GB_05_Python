"""
Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""


def arithmetic_progression(start: int, step: int, count: int) -> list:
    return [i for i in range(start, start + count * step, step)]


def is_digit(text: str) -> int:
    while True:
        num = input(text)
        try:
            int(num)
            return int(num)
        except ValueError:
            print('Необходимо ввести целое число!')


if __name__ == '__main__':
    start_el = is_digit('Введите первый элемент: ')
    step_el = is_digit('Введите разность: ')
    el_count = is_digit('Введите количество элементов: ')
    arithmetic_progression_list = arithmetic_progression(start_el, step_el, el_count)
    print(*arithmetic_progression_list)
