"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""

from random import randint as rand


def set_in_set():
    print('<--Параметры первого списка-->')
    first_set = set_generator()
    print('<--Параметры второго списка-->')
    second_set = set_generator()
    print(f'Первый список уникальных значений: {first_set}')
    print(f'Второй список уникальных значений: {second_set}')
    output_list = [i for i in first_set if i in second_set]
    print('<--Список повторяющихся значений-->')
    return sorted(output_list)


def set_generator() -> set:
    set_len = int(input('Введите длину списка: '))
    max_count = int(input('Введите максимальное генерируемое число: '))
    return set(rand(1, max_count) for _ in range(set_len))


if __name__ == '__main__':
    print(set_in_set())
