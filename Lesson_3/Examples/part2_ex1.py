# bin search


def bin_search(array, value):
    left = 0
    right = len(array) - 1
    pos = len(array) // 2

    while array[pos] != value and left <= right:
        if value < array[pos]:
            right = pos - 1
        else:
            left = pos + 1
        pos = (right + left) // 2

    return None if left > right else pos


array = [1, 2, 5, 7, 8, 19, 32, 45, 67, 99, 100]
print(bin_search(array, 9))
