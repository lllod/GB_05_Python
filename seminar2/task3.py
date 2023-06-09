"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
*** (1)У вас есть массив чисел, составьте из них максимальное число. Например:
                                 [61, 228, 9] -> 961228
***(2)У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке. Вы можете вставлять между ними знаки «+», «-» или
ничего. У вас будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.

10 -> 1 2 4 8
"""

from itertools import permutations


def num_isdigit() -> int:
    while True:
        user_num = input('Введите число N: ')
        try:
            user_num.isdigit()
            return int(user_num)
        except ValueError:
            print('Введите целое положительное число!')


def num_exponent() -> list:
    num = num_isdigit()
    return [2 ** i for i in range(num) if 2 ** i <= num]


def max_num(nums_list: list) -> int:
    return int(max(''.join(i) for i in permutations(str(i) for i in nums_list)))


if __name__ == '__main__':
    # print(num_exponent())
    nums_list = [61, 228, 9]
    print(max_num(nums_list))
