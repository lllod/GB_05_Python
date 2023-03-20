"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
минимальное количество монет, которые нужно перевернуть
5 -> 1 0 1 1 0
2
"""
from random import randint as rand
from collections import Counter


def list_create() -> list:
    coins = coins_count()
    coins_list = [rand(0, 1) for i in range(coins)]
    print(f'Список монет: {coins_list}')
    return coins_list


def coins_count() -> int:
    while True:
        coins = input('Введите количество монет: ')
        try:
            return int(coins)
        except ValueError:
            print('Необходимо ввести целое положительное число!')


def heads_or_tails() -> int:
    coins_dict = Counter(list_create())
    return coins_dict.most_common()[1][1]


if __name__ == '__main__':
    print(f'Минимальное количество монет, которое нужно перевернуть: {heads_or_tails()}')
