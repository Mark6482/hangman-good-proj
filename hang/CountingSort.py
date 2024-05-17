def russian_alphabet_counting_sort(input_string, russian_alphabet):
    # Определяем диапазон символов русского алфавита
    min_char = 'а'
    max_char = 'я'
    range_size = ord(max_char) - ord(min_char) + 1

    # Создаем словарь для подсчета количества каждого символа
    count = {}

    # Подсчитываем количество каждого символа во входной строке
    for char in input_string:
        if min_char <= char <= max_char:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    # Формируем отсортированную строку на основе словаря с подсчитанными символами
    sorted_string = []
    for char in russian_alphabet:
        if char in count:
            sorted_string.append(char * count[char])

    return ''.join(sorted_string)
