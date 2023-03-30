"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех
арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4
"""


# def rec_sum(first_num: int, second_sum: int) -> int:
#     return first_num + (1 if rec_sum(first_num, second_sum - 1) else 0)
#
#
# if __name__ == '__main__':
#     first_num = int(input('Введите первое число: '))
#     second_sum = int(input('Введите второе число: '))
#     print(rec_sum(first_num, second_sum))