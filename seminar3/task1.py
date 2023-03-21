"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой
строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""

from collections import Counter
from random import randint as rand


def list_create() -> list:
    print('Введите длину списка:', end=' ')
    list_length = num_isdigit()
    nums_list = [rand(0, list_length) for i in range(list_length)]
    print(f'Список чисел: {nums_list}')
    return nums_list


def num_isdigit() -> int:
    while True:
        num = input()
        if num.isdigit() and int(num) > 0:
            return int(num)
        print('Необходимо ввести целое положительное число!')


def num_found() -> int:
    print('Введите искомое число:', end=' ')
    num_found = num_isdigit()
    return Counter(list_create())[num_found]


if __name__ == '__main__':
    print(num_found())
