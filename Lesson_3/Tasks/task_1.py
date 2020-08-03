# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

array = [i for i in range(2, 100)]
divider = [[i for i in range(2, 10)] for _ in range(2)]

for i in range(8):
    divider[1][i] = 0

for item in array:
    for i in range(8):
        divider[1][i] = divider[1][i] + 1 if item % divider[0][i] == 0 else divider[1][i]

for column in divider:
    for item in column:
        print(f"{item:>4}", end="")
    print()
