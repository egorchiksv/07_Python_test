# Файл содержит данные о продажах товаров:
# каждая строка предстваляет собой запись о проданном товаре в формате "Наименование товара - Количество проданных едений".
# Задача: Напишите программу на Python, которая открывает текстовый файл sales.txt, читает его содержимое и выводит общее
# количество проданных единиц для каждого товара.

def analyze_sales(filename):
    sales_data = {}


    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue # Пропускаем пустые строки
            product, quantity = line.split("-")
            quantity = int(quantity)


        if product in sales_data:
            sales_data[product] += quantity
        else:
            sales_data[product] = quantity


    for product, total_sales in sales_data.items():
        print(f"{product}: Общие продажи - {total_sales}")


# Пример вызова функции
analyze_sales("salex.txt")