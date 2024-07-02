"""9. Поданному целому неотрицательному n вычислите значение n!. N!=1*2*3*...N (произведение всех чисел от 1 до N) 0!=1.
Решить задачу использую цикл while

Input: 5
Output: 120"""

# n = int(input())
# i = 1
# result = 1
# while i <= n:
#     result *= i
#     i += 1
# print(result)

"""Дано натуральное число A>1. Определите, каким по счету чилом Фибаначчи оно является, т.е. выведете такое число n, что
f(n)=A. Если A не является числом Фибоначчи, выведите число -1.
Фибоначчи: 0 1 1 2 3 5 8 13 ...
Input: 5
Output: 6"""

# n = int(input())
# n0 = 0
# n1 = 0
# n2 = 1
# i = 2
# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = -1
# print(i)

"""Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений
за погодой. Они обратились к синоптикам, а те, в свою очередь, занались исследованиями статистики за прошлые годы. Их интересует,
сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно 
превышала 0 градусов Цельсия. Напишите программу, помогающую синоприткам в работе.
Пользователь вводи число N - общее количество рассматриваемых дней (1 <= N <= 100). В следующих строках располагается N целых чисел.
Каждое число - среднесуточная температура в ссответствующий день. Температура - целые числа и лежат в диапазоне от -50 до 50

Input: 6 -> -20 30 -40 50 10 -10
Output: 2"""

# n = int(input())
# k = 0
# max = 0
# for i in range(n):
#     x = int(input())
#     if x > 0:
#         k += 1
#     else:
#         if max < k:
#             max = k
#         k = 0
# print(max)

"""Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать
арбуз потяжелей, а для тещи полегче. Но вот не задача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый
арбуз? Помогите ему!

Пользователь вводи одно число N - количество арбузов. Вторая строка содержит N чилес, записанных на новой строчке каждое. Здесь каждое
число - это масса соответствующего арбуза. Все числа натуральные и не превышают 3000

Input: 5 -> 5 1 6 5 9
Output: 1 9"""

# n = int(input())
# max = -1
# min = 30001
# for i in range(n):
#     x = int(input())
#     if x > max:
#         max = x
#     if x < min:
#         min = x
# print(max, min)