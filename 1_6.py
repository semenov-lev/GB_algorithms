# 1.6 Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

wanted_letter_position = input("Введите номер искомой английской буквы в диапазоне от 1 до 26: ")

corrective = ord("a") - 1
first_letter_position = ord("a") - corrective
last_letter_position = ord("z") - corrective

try:
    wanted_letter_position = int(wanted_letter_position)
    if first_letter_position <= wanted_letter_position <= last_letter_position:
        letter = chr(int(wanted_letter_position) + corrective)
        print(f"Под этим номером располагается буква '{letter}'")
    else:
        print("В алфавите 26 букв, выбор в диапазоне от 1 до 26!")
except ValueError:
    print("Некорректный ввод!")
