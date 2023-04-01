"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Диапазон от 6 до 12
Вывод: [1, 9, 13, 14, 19]
"""
from random import randint as rand


def nums_range(index: int) -> list:
    el_list = [rand(-20, 20) for _ in range(index)]
    print(f'Начальный список: {el_list}')
    return [i for i, val in enumerate(el_list) if min_el <= val <= max_el]


def is_digit(text: str) -> int:
    while True:
        num = input(text)
        try:
            int(num)
            return int(num)
        except ValueError:
            print('Необходимо ввести целое число!')


if __name__ == '__main__':
    min_el = is_digit('Введите минимальное значение: ')
    max_el = is_digit('Введите максимальное значение: ')
    max_index = is_digit('Введите количество элементов: ')
    print(f'Список с индексами значений, которые принадлежат заданному диапазону:\n{nums_range(max_index)}')
