# def f(x):
#     return x*x

# a = f
# print(a(5))
# print(f(5))

# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a, b: a + b

# math(lambda a, b: a + b, 5, 45)
# -----------------------------------------------------------------------------------------
"""1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]"""

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

#--------------------------------------------------------------------------------------------

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

#-----------------------------------------------------------------

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

#-----------------------------------------------------------------------

"""Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?"""

# data = '15 156 96 3 5 8 52 5'
# print(data)

# data = data.split()
# print(data)

# data = list(map(int, data.split()))
# print(data)

#-------------------------------------------------------------------------------

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#-------------------------------------------------------------------------------

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

#-------------------------------------------------------------------------------

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#-------------------------------------------------------------------------------

# colors = ['red', '8898', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()