# Напишите программу на Python, которая выполняет следующие действия
#1) Имеется список чисел numbers, который содержит значения от 1 до 100.
#2) Вам нужно создать новый список squared_numbers, в который войдут квадраты всех четных чисел из numbers.
#3) Затем создайте список cubed_numbers, содержащий кубы всех чисел из squared_numbers, которые делятся на 3.
#4) Вывести сумму всех чисел из cubed_numbers.
numbers = list(range(1, 101))
# Создаем список квадратов четных чисел
squared_numbers = []
for number in numbers:
    if number % 2 == 0:
        squared_numbers.append(number ** 2)


# Создаем список кубов чисел из squared_numbers, которые делятся на 3
cubed_numbers = []
for number in squared_numbers:
    if number % 3 == 0:
        cubed_numbers.append(number ** 3)


# Вычисляем сумму всех чисел в списке cubed_numbers
sum_of_cubed_numbers = sum(cubed_numbers)

squared_numbers1 = [num ** 2 for num in range(2, 101, 2)]

# Создаем список кубов чисел из squared_numbers, которые делятся на 3
cubed_numbers1 = [num ** 3 for num in squared_numbers1 if num % 3 == 0]

# Вычисляем сумму всех чисел в списке cubed_numbers
sum_of_cubed_numbers1 = sum(cubed_numbers1)

print(sum_of_cubed_numbers)
print(sum_of_cubed_numbers1)