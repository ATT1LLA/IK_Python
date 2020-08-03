# Поменять местами главную и побочную диагонали матррицы

import random

size = 5

matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]


def print_matrix(matrix):
    for line in matrix:
        for item in line:
            print(f"{item:>4}", end='')
        print()


print_matrix(matrix)

for i in range(size):
    for j in range(size):
        if i == j:

            spam = matrix[i][j]
            matrix[i][j] = matrix[i][size - 1 - j]
            matrix[i][size - 1 - j] = spam

print("-" * size * 4)
print_matrix(matrix)