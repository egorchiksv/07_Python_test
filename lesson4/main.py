# list_1 = []
# list_1 = list()
# print(list_1)

# list_1 = [1, 2, 3, 8]
# print(*list_1) # открывыем список и выводим значение через пробел

# for i in list_1:
#     print(i)

# print(len(list_1))

# print(list_1[3])

# print(list_1[-1]) # вывод с конца

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # добавляем элемент в конец списка
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

#Удаление последнего элемента
# list_1 = [12, 7, -1, 21, 0]
# a = list_1.pop()
# print(list_1.pop()) # 0 удаляем последнюю цифру и выводит удалаемую цифру
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# Удаление конкретного элемента из списка
#
# print(list_1.pop(1)) # 7
# print(list_1) # [12, -1, 21, 0]

# Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2,11)) # на вторую позицию вставляем число 11
# print(list_1) # [12, 7, 11, -1, 21, 0]

"""Срез списка
Помните в конце первой лекции Вы прошли срезы строк? Также существует срез списка,
давайте научимся изменять наш список
● Отрицательное число в индексе — счёт с конца списка"""

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]

# t = () # объявляем пустой картеж
# print(type(t))

# t = (1, 5, 3,)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v) # преобразовываем в картеж
# print(v)
# print(type(v))
# a, b = 1, 2
# a = b = 1
# a,b,c = v # распаковываем картеж и записываем в каждую переменную по элементу
# print(a, b, c)

# t = (1, 2, 3, 5,)
# print(t[1])
# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# d = {} # объявляем словарь
# d = dict() # объявляем словарь

# d['q'] = 'qwerty' # записываем значение 'qwerty' с ключем 'q'
# print(d)

# d['w'] = 'werty'
# print(d)

# print(d['q'])

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left']) # ← типы ключей могут отличаться
# # print(dictionary['up']) # ↑ типы ключей могут отличаться
# # dictionary['left'] = '⇐'
# # print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# # for item in dictionary:
# #     print('{}: {}'.format(item, dictionary[item]))
# #    print(item)
# print(dictionary.items()) # выводит в виде картежа
# for (k,v) in dictionary.items():
#     print(k, v)

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# colors.clear() # { }
# print(colors) # set()

# q = set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединяет, записывает только уникальные значения
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a) # замораживаем множество, т.к. в дальнейшем мы не сможем его изменять
# print(b) # frozenset({1, 2, 3, 5, 8})

"""Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
Решение:
1. Создать список чисел от 1 до 100"""
# list_1 = []
# for i in range(1, 101):
# list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# # Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# # 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
# # Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# # Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

