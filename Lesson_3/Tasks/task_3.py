# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

begin_with = 1
end_with = 20
array = [random.randint(begin_with, end_with) for _ in range(10)]

print(f"Before: {array}")

max_elem = begin_with - 1
max_id = 0
min_elem = end_with + 1
min_id = 0

for i in range(10):

    if array[i] > max_elem:
        max_elem = array[i]
        max_id = i

    if array[i] < min_elem:
        min_elem = array[i]
        min_id = i

if max_id != min_id:
    array[min_id] = max_elem
    array[max_id] = min_elem

print(f"After:  {array}")
