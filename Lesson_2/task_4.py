# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input("Type number of components: "))
number = 1
summ = 0

for i in range(n):
    summ += number
    number /= -2

print(summ)

# Хочу посмотреть на изменения в git
