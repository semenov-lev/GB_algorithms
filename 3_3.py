# 3.3 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = []
i = 0

while i < 20:
    a.append(random.randint(0, 10))
    i += 1

print(f"Первичный массив:  {a}")

a_max = max(a)
a_min = min(a)

i = 0
# Алгоритм на случай дублирования случайных значений
for el in a:
    if el == a_max:
        a[i] = a_min
    if el == a_min:
        a[i] = a_max
    i += 1

print(f"Измененный массив: {a}")
print(f"Max: {a_max}\nMin: {a_min}")
