"""1. За день машина проезжает n километров. Сколько дней нужно машине, чтобы проехать маршрут длиной m километров? 
 При решении этой задачи нельзя пользоваться условной инструкцией if или циклами
 Input:
 n = 700
 m = 750
 Output:
 2"""

# n = int(input())
# m = int(input())
# print((m + n - 1)//n)

"""3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
 За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее
 число парт, которое нужно приобести для них.
 Input: 20 21 22(ввод чисел НЕ в одну строку)
 Output: 32"""

# a = int(input())
# b = int(input())
# c = int(input())
# s1 = (a + 1)//2
# s2 = (b + 1)//2
# s3 = (c + 1)//2
# print(s1 + s2 + s3)

"""5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от "головы"
 поезда, а иногда - с "хвоста"; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
 Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов 
 в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать не возможно.
 Input: 3 4 (ввод на разных строках)
 Output: 6"""

# i = int(input())
# j = int(input())
# if i - j == 0:
#     print(-1)
# else:
#     print(i + j - 1)

"""7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным,
 то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если
 его номер кратен 4, но не кратен 100, а также если он кратен 400.
 Input: 2016
 Output: YES"""

n = int(input())
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("YES")
else:
    print("NO")