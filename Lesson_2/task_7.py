# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import random

count = int(input("Type number of checks: "))

for i in range(count):
    summ = 0
    n = random.randint(1, 1000)

    for j in range(n + 1):
        summ += j

    print(f"{i + 1}. 1 + .. + {n} = {summ} || n * (n + 1) / 2 = {int(n * (n + 1) / 2)}")
