"""
Даны числа a и b. Определите, сколько существует последовательностей из a нулей и b единиц, в которых никакие два нуля
не стоят рядом.
Ввод 5 8
Вывод 126
"""


def sequence(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 1
    elif a > b + 1:
        return 0
    return sequence(a, b - 1) + sequence(a - 1, b - 1)


def is_digit(text: str) -> int:
    while True:
        num = input(text)
        try:
            int(num)
            return int(num)
        except ValueError:
            print('Необходимо ввести целое число!')


if __name__ == '__main__':
    first_num = is_digit('Ведите первое число: ')
    second_num = is_digit('Ведите второе число: ')
    print(sequence(first_num, second_num))
