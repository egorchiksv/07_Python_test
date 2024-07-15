# Сколько слов в файле input.txt

def count_words_imperative(filename):
    word_count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count


# Вызов функции
count = count_words_imperative('input.txt')
print(f"Количество слов в файле: {count}")