"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в
первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых
чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""
from random import randint as rand


def list_create() -> tuple:
    print('Введите длину списка:', end=' ')
    list_length = num_isdigit()
    nums_list = [rand(0, list_length) for i in range(list_length)]
    print(f'Список чисел: {nums_list}')
    return nums_list, list_length


def num_isdigit() -> int:
    while True:
        num = input()
        if num.isdigit() and int(num) > 0:
            return int(num)
        print('Необходимо ввести целое положительное число!')


def num_modul() -> int:
    print('Введите число:', end=' ')
    user_num = num_isdigit()
    num_list, max_modul = list_create()
    num_modul = 0
    for i in num_list:
        if user_num - i == 0:
            return user_num
        elif abs(user_num - i) < max_modul:
            max_modul = abs(user_num - i)
            num_modul = i
    return num_modul


if __name__ == '__main__':
    print(num_modul())
