# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input("Type one integer: "))
even_counter = 0
odd_counter = 0

while number:
    digit = number % 10
    if digit % 2:
        odd_counter += 1
    else:
        even_counter += 1
    number //= 10

print(f"Even digits: {even_counter}\n"
      f"Odd digits: {odd_counter}")
