# 3.7 В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

a = [random.randint(-10, 10) for _ in range(8)]

print(f'original list:\n{a}')

first_min = min(a)

if a.count(first_min) > 1:
    print(f'Первое и второе минимальные числа: {first_min}')
else:
    second_min = min(list(filter(lambda b: b != first_min, a)))
    print(f'Первое минимальное число: {first_min}, второе: {second_min}')
