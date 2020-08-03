# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random

array = [random.randint(1, 20) for _ in range(10)]
even_id = []

for i in range(10):
    if array[i] % 2 == 0:
        even_id.append(i)

print(f"Array:    {array}")
print(f"Even ids: {even_id}")
