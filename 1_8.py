# 1.8 Определить, является ли год, который ввел пользователь, високосным или невисокосным.

year = input("Введите год: ")

try:
    year = int(year)
except TypeError:
    print("Некорректный ввод!")
else:
    leap_year = f'{year} – високосный год'
    not_leap_year = f'{year} – не високосный год'
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(leap_year)
            else:
                print(not_leap_year)
        else:
            print(leap_year)
    else:
        print(not_leap_year)
