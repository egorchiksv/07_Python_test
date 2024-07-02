# n = 1.89

# print(n)

# n = 'dsafasd'

# print(n)

# n = 5
# print(type(n))

# n = 'fd\'asdf'
# print(n)

# n = 'fd"adsfasdf"sdf'
# print(n)

# print(5)
# print(5)
# print(5)
"""
print(5)
"""

# print(5, 8)
# print(5) Комментирование нескольких строк делается Ctrl+K затем сразуже Ctrl+C. Чтобы раскоменчивать выделенное Ctrl+K затем Ctrl+U
# print(5, 9)

# a = 5
# b = 5.89
# c = 'hello'

# print(a,b,c)
# print(a,' - ',b,' - ',c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# print('Введите первое число: ')
# a = input()

# b = input('Введите второе число: ')

# print(a, ' + ', b, ' = ', a + b)

# c = 5.89
# print(c)
# n = int(c)
# print(n)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c + '89')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# print('Введите первое число: ')
# a = int(input())

# b = int(input('Введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

# a = 5.89956
# b = 6.55655
# print(round(a*b, 3))

# iter = 2 
# iter += 3 # iter = iter + 3 
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5 целая часть от деления
# iter %= 5 # iter = iter % 5 остаток от деления
# iter **= 5 # iter = iter ** 5 возведение в степень 5

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # Выводит сумму цифр чилса n

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при деления числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может преавышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# r = range(100, 0, -20)
# for i in r:
#     print(i)

# for i in 'qwerty':
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё', 'ЕЩЁ'))

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                      # с
# print(text[1])                      # ъ
# print(text[len(text)-1])            # к
# print(text[-1])                     # - означает выводить с конца
# print(text[-5])                     # б
# print(text[:])                      # съешь ещё этих мягких французских булок - Выводит абсолютно все символы
# print(text[:2])                     # cъ - означает что выводим с начала и на указанное количество символов
# print(text[len(text)-2:])           # ок - означает, что выводим до конца
# print(text[20:])                    # х французских булок - выводит с 20 символа и до конца
# print(text[2:9])                    # ешь ещё
# print(text[6:-18])                  # ещё этих мягких - начинаем с 6 и начиная с конца -18 и идем до 6
# print(text[0:len(text):6])          # сеикакл - начинаем с 0 идем с конца с шагом 6
# print(text[::6])                    # сеикакл - начинаем с 0 идем с конца с шагом 6
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)