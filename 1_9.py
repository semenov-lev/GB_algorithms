# 1.9 Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = input("Введите первое число: ")
b = input("Введите второе число: ")
c = input("Введите третье число: ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
except TypeError:
    print("Некорректный ввод!")
else:
    if b < a < c or b > a > c:
        print(f'Среднее число: {a}')
    else:
        if a < b < c or a > b > c:
            print(f'Среднее число: {b}')
        else:
            if a < c < b or a > c > b:
                print(f'Среднее число: {c}')
            else:
                print("Числа должны быть разными")
