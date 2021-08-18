# 2.5 Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


stamp = ""
stamp_counter = 0
start = 32
end = 127

for code in range(start, end + 1):
    stamp_counter += 1
    stamp += f" '{code} – {chr(code)}' "
    if stamp_counter == 10:
        print(stamp)
        stamp = ""
        stamp_counter = 0
    if code == end:
        print(stamp)
