# Divide array in two arrays with elems larger zero and below zero

import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

array_below_zero = []
array_larger_zero = []

for elem in array:

    if elem > 0:
        array_larger_zero.append(elem)
    elif elem < 0:
        array_below_zero.append(elem)

print(array_below_zero)
print(array_larger_zero)