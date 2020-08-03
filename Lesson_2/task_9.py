# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

count = int(input("Type number of integers: "))

maximum_sum = 0
maximum_number = 0
counter = 0

for i in range(count):
    number = int(input(f"Number №{i + 1}: "))
    number_copy = number
    counter = 0

    while number:
        counter += number % 10
        number //= 10

    if counter > maximum_sum:
        maximum_sum = counter
        maximum_number = number_copy
    elif counter == maximum_sum:
        # Можно как-то это реализовать, но не без использования массивов
        pass

print(f"Biggest digit sum = {maximum_sum} from number = {maximum_number}.")
