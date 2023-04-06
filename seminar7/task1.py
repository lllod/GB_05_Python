"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
порядке и “Пам парам”, если с ритмом все не в порядке
*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам
"""

import re


def is_vowels(letter: str) -> int:
    if re.match(r'[ауоыиэяюёе]', letter.lower()):
        return 1
    return 0


def is_rhythm(user_phrase: str) -> str:
    phrase_list = user_phrase.replace('-', '').split()
    for i in range(len(phrase_list)):
        if sum(is_vowels(k) for k in phrase_list[i]) % 2 != 0:
            return 'Пам парам'
    return 'Парам пам-пам'


if __name__ == '__main__':
    phrase = input('Введите фразу: ')
    print(is_rhythm(phrase))
