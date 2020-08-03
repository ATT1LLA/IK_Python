# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number = int(input("Type an integer: "))
reversed_number = 0

while number:
    reversed_number *= 10
    reversed_number += number % 10
    number //= 10

print(reversed_number)
