# 4. Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(0, 10) for _ in range(30)]

print(f"Array: {array}")

number_dict = {}

for item in set(array):
    number_dict[item] = 0

for item in array:
    number_dict[item] += 1

max_count = 0
max_key = 0

for key in number_dict:
    if number_dict[key] > max_count:
        max_count = number_dict[key]
        max_key = key

print(f"Element {max_key} is most common in array. It's located there {max_count} times")
