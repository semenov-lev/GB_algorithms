# 1.4 Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random


integer_range = input("Задайте диапазон для генерации целого числа, например: '0/100' ")
real_number_range = input("Задайте диапазон для генерации вещественного числа, например: '0.5/50.09' ")
symbols_range = input("Задайте диапазон для генерации символа, например: 'a/z' ")

try:
    integer_range = (int(integer_range.split('/')[0]), int(integer_range.split('/')[1]))
    real_number_range = (float(real_number_range.split('/')[0]), float(real_number_range.split('/')[1]))
    symbols_range = (ord(symbols_range.split('/')[0].lower()), ord(symbols_range.split('/')[1].lower()))
except ValueError:
    print("Некорректный ввод!")
else:
    rand_int = random.randint(integer_range[0], integer_range[1])
    rand_real = random.uniform(real_number_range[0], real_number_range[1])
    rand_symbol = chr(random.randint(symbols_range[0], symbols_range[1]))
    print(f"Случайное целое число: {rand_int}")
    print(f"Случайное вещественное число: {rand_real}")
    print(f"Случайный символ: {rand_symbol}")
