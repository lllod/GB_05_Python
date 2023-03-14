"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""


def chocolate_size() -> tuple:
    while True:
        chocolate_n = input('Введите n: ')
        chocolate_m = input('Введите m: ')
        chocolate_k = input('Введите k: ')
        if int(chocolate_n) > 0 and int(chocolate_m) > 0 and int(chocolate_k) > 0:
            return int(chocolate_n), int(chocolate_m), int(chocolate_k)
        else:
            print('Введите натуральные числа!')


def chocolade_chunks() -> str:
    chocolate_n, chocolate_m, chocolate_k = chocolate_size()
    if (chocolate_k % chocolate_n == 0 or chocolate_k % chocolate_m == 0) and chocolate_k < chocolate_m * chocolate_n:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(chocolade_chunks())
