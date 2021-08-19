# 3.1 В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

counter = 0

for a_num in range(2, 200):
    for b_num in range(2, 10):
        b_counter = 0
        if a_num % b_num == 0:
            b_counter += 1
        else:
            break
        if b_counter == 7:
            counter += 1

print(f"{counter} чисел")
