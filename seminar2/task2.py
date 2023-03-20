"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он
задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он
называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
"""


def brother_nums() -> tuple:
    while True:
        sum = input('Введите сумму чисел: ')
        mult = input('Введите произведение чисел: ')
        if int(sum) <= 1000 and int(mult) <= 1000:
            return int(sum), int(mult)
        else:
            print('Введите целые положительные числа до 1000!')


def sister_nums() -> tuple:
    sum, mult = brother_nums()
    a = sum // 2
    b = sum - a
    while True:
        if not a or not b:
            break
        elif mult != a * b:
            a -= 1
            b += 1
        else:
            return a, b


if __name__ == '__main__':
    try:
        a_b_nums = sister_nums()
        print(f'Петя загадал: {a_b_nums[0]} и {a_b_nums[1]}')
    except TypeError:
        print('Заданы некорректные условия!')
    except ValueError:
        print(print('Заданы некорректные условия!'))
