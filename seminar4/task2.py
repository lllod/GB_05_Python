"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед
некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
"""

from random import randint as rand


def max_count_berries() -> int:
    bushes_list = bushes_generate()
    print(f'Список кустов: {bushes_list}')
    max_count_berries = 0
    for i in range(1, len(bushes_list) - 1):
        temp_max = bushes_list[i - 1] + bushes_list[i] + bushes_list[i + 1]
        if temp_max > max_count_berries:
            max_count_berries = temp_max
    print('Максимальное количество ягод:', end=' ')
    return max_count_berries


def bushes_generate() -> list:
    bushes_count = int(input('Введите количество кустов: '))
    berries_list = [rand(1, 10) for _ in range(bushes_count)]
    berries_list.insert(0, berries_list[-1])
    berries_list.append(berries_list[1])
    return berries_list


if __name__ == '__main__':
    print(max_count_berries())
