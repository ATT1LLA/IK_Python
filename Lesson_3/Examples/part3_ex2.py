# Add elem into array with it's value and position

import random

array_1 = [random.randint(-100, 100) for _ in range(10)]
print(array_1)


def add_elem(array: list, elem: int, position: int) -> list:
    array.append(None)
    i = len(array) - 1

    while i > position:
        array[i] = array[i - 1]
        i -= 1

    array[position] = elem

    return array


elem = int(input("Type elem u want to add to the array: "))
position = int(input("Type position of this elem: "))

print(add_elem(array_1, elem, position))
