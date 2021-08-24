# 3.8 Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

try:
    for n in range(5):
        matrix.append([])
        for el in range(4):
            matrix[n].append(int(input(f"Введите число [{n + 1}][{el + 1}]: ")))
        matrix[n].append(sum(matrix[n]))
    for n in matrix:
        print('\n', end="")
        for el in n:
            print(el, end="     ")
        print('\n', end="")
except ValueError:
    print("Некорректный ввод!")
