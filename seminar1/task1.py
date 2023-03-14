"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
*** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного
"""


def digits_sum():
    num = is_digit().replace('.', '')
    digits_sum = 0
    for i in num:
        digits_sum += int(i)
    return digits_sum


def is_digit():
    while True:
        num = input('Введите число: ')
        try:
            float(num)
            return num
        except ValueError:
            print('Необходимо ввести число!')


if __name__ == '__main__':
    print(digits_sum())
