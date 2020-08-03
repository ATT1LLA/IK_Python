# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

count = int(input("Type number of integers: "))
searching_for = int(input("The number we are looking for: "))

counter = 0

for i in range(count):
    number = int(input(f"Number №{i + 1}: "))

    while number:
        counter = counter + 1 if number % 10 == searching_for else counter
        number //= 10

print(counter)
