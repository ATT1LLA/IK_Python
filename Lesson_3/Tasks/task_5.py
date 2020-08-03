# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

border = 10
array = [random.randint(-border, border) for _ in range(10)]

print(f"Array: {array}")

max_elem = -border - 1

for item in array:
    max_elem = item if 0 > item > max_elem else max_elem

if max_elem != -border - 1:
    print(f"The biggest negative item in array: {max_elem}")
else:
    print("There is no negative number in array.")
