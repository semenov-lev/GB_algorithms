# 3.9 Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []
min_elements = []

for i in range(5):
    matrix.append([])
    for el in range(5):
        matrix[i].append(random.randint(10, 40))

for n in matrix:
    print('\n', end="")
    for el in n:
        print(el, end="     ")
    print('\n', end="")

for i in range(5):
    column = []
    for line in matrix:
        column.append(line[i])
    min_elements.append(min(column))

print(f'\nМинимальные элементы столбцов: {min_elements}\nМаксимальный элемент, среди них: {max(min_elements)}')
