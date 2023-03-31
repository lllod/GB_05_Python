"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def exponentiation(number: int, num_to_exp: int) -> int:
    if num_to_exp == 0:
        return 1
    return number * (exponentiation(number, num_to_exp - 1) if num_to_exp > 2 else number)


if __name__ == '__main__':
    num = int(input('Введите число: '))
    to_exp = int(input('Введите степень числа: '))
    print(exponentiation(num, to_exp))
