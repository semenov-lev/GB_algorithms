# 1.5 Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

alphabet = "abcdefghijklmnopqrstuvwxyz"

wanted_letter = input("Введите две искомые английские буквы, например: 'b-f' ")

try:
    letter_1 = wanted_letter.split('-')[0].lower()
    letter_2 = wanted_letter.split('-')[1].lower()
    letters_between = ord(letter_2) - ord(letter_1) - 1
except Exception:
    print("Некорректный ввод!")
else:
    if len(wanted_letter) == 3 and letter_1 in alphabet and letter_2 in alphabet:
        print(f'Буква "{letter_1}" – {ord(letter_1) - 96}-я по счету, '
              f'"{letter_2}" – {ord(letter_2) - 96}-я по счету, в английском алфавите. '
              f'Букв между ними: {letters_between if letters_between > -1 else "0"}')
    elif len(wanted_letter) > 3:
        print("Вы ввели лишние символы")
    else:
        print("Введенные Вами символы не являются частью английского алфавита!")
