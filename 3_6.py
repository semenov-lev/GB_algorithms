# 3.6 В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(-50, 50) for _ in range(8)]

print(f'original list:\n{a}')

a_min = min(a)
a_max = max(a)
min_idx = a.index(a_min)
max_idx = a.index(a_max)
counter = 0

print(f'min: {a_min}')
print(f'max: {a_max}')

if abs(max_idx - min_idx) > 1:

    if min_idx < max_idx:
        a_sort = a[min_idx + 1:max_idx]
        print(f'sorter list:\n{a_sort}')
        for el in a_sort:
            counter += el
    elif min_idx > max_idx:
        a_sort = a[max_idx + 1:min_idx]
        print(f'sorter list:\n{a_sort}')
        for el in a_sort:
            counter += el
    print(f'Сумма элементов: {counter}')

else:
    print('Между минимальным и максимальным элементами, нет элеменов')
