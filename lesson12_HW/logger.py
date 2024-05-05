from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберете вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    
    if var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
    
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        print(''.join(data_first_list))
                
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def change_data():
    list1 = []
    list2 = []
    title = ["1 - Имя", "2 - Фамилия", "3 - Телефон", "4 - Адрес"]
    search = input('Введите данные для поиска: ')
    var = int(input(f"В каком файле будем искать данные в 1 или во 2: "))
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
        print(data_first)
        l = len(data_first)
        i = 0
        while i < l:
            for j in range(4):
                list1.append(data_first[j][0:len(data_first[j])-1])
            if search in list1:
                list2 += list1
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*title))
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*list1))
            list1.clear()
            del data_first[0:5]
            i += 5
        list1.clear()
        var1 = input("Введите номер столбца, который нужно изменить: ")
        change = input("Введите измененные данные: ")
        new_line = list2
        list2 = "\n".join(str(e) for e in list2) + "\n"
        if var1 == '1':
            new_line[0] = change
        if var1 == '2':
            new_line[1] = change
        if var1 == '3':
            new_line[2] = change
        if var1 == '4':
            new_line[3] = change
        print('| {:8} | {:12} | {:20} | {:15} |'.format(*title))
        print('| {:8} | {:12} | {:20} | {:15} |'.format(*new_line))
        new_line = "\n".join(str(e) for e in new_line) + "\n"
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            file1 = f.read()
            file2 = file1.replace(list2, new_line)
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write(file2)

    if var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            res = f.readlines()
        for line in res:
            line = line.split(";")
            if search in line:
                old_line = ";".join(str(e) for e in line)
                line[3] = line[3][0:len(line[3])-1]
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*title))
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*line))
                var1 = input("Введите номер столбца, который нужно изменить: ")
                change = input("Введите измененные данные: ")
                new_line = line
                if var1 == '1':
                    new_line[0] = change
                if var1 == '2':
                    new_line[1] = change
                if var1 == '3':
                    new_line[2] = change
                if var1 == '4':
                    new_line[3] = change
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*title))
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*new_line))
        new_line = ";".join(str(e) for e in new_line) + "\n"
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            file1 = f.read()
            file2 = file1.replace(old_line, new_line)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(file2)            
    
def delete_data():
    list1 = []
    list2 = []
    title = ["1 - Имя", "2 - Фамилия", "3 - Телефон", "4 - Адрес"]
    search = input('Введите данные для поиска: ')
    var = int(input(f"В каком файле будем искать данные в 1 или во 2: "))
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
        print(data_first)
        l = len(data_first)
        i = 0
        while i < l:
            for j in range(4):
                list1.append(data_first[j][0:len(data_first[j])-1])
            if search in list1:
                list2 += list1
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*title))
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*list1))
            list1.clear()
            del data_first[0:5]
            i += 5
        list1.clear()
        list2 = "\n".join(str(e) for e in list2) + "\n"
        print(list2)
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            file1 = f.read()
            file2 = file1.replace(list2, '')
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write(file2)
        print("Запись удалена из файла")

    if var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            res = f.readlines()
        for line in res:
            line = line.split(";")
            if search in line:
                old_line = ";".join(str(e) for e in line)
                line[3] = line[3][0:len(line[3])-1]
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*title))
                print('| {:8} | {:12} | {:20} | {:15} |'.format(*line))
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            file1 = f.read()
            file2 = file1.replace(old_line, '')
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(file2) 