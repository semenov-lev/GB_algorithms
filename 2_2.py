# 2.2 Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even_counter = 0
odd_counter = 0

a = input("Введите число: ")

if a.isdigit():
    for _ in str(a):
        if int(_) % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    print(f"В числе {a}, {even_counter} четных и {odd_counter} нечетных цифр")
else:
    print("Необходимо ввести число!")
