"""
Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел, сумма цифр которых равна s.
Запись натурального числа не может начинаться с цифры 0.
В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.
3 15 -> 69
4 16 -> 564
2 3 -> 3
6, 40 ->10746
"""


def suitable_numbers(a: int, b: int) -> int:
    return len([i for i in range(10 ** (a - 1), 10 ** a) if sum(int(k) for k in list(str(i))) == b])


if __name__ == '__main__':
    first_num = int(input('Введите a: '))
    second_num = int(input('Введите b: '))
    print(suitable_numbers(first_num, second_num))
