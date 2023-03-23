"""
*****(3)Напишите программу, которая принимает на вход две строки и определяет, являются ли они анаграммами.
Знаки препинания, пробелы и регистр при этом игнорируются.
Пример ввода:
Цари, вино и сало.
Лисица и ворона.
Пример вывода:
YES
"""
from collections import Counter


def is_anagrams() -> str:
    first_words = list(''.join(i.upper() for i in input('Введите первую фразу: ') if i.isalpha()))
    second_words = list(''.join(i.upper() for i in input('Введите вторую фразу: ') if i.isalpha()))
    return 'YES' if Counter(first_words) == Counter(second_words) else 'NO'


if __name__ == '__main__':
    print(is_anagrams())
