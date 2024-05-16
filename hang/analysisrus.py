from collections import defaultdict
import string
from .models import Word 

def russian_alphabet_frequency_analysis():
    words = Word.objects.all()
    # Создаем словарь для подсчета частоты встречаемости букв русского алфавита
    frequency = defaultdict(int)
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    total_letters_count = 0 

    for word in words:
        for char in word.text.lower(): 
            if char in russian_alphabet: 
                frequency[char] += 1
                total_letters_count += 1
    percentage_frequency = {}

    for char, count in frequency.items():
        percentage = (count / total_letters_count) * 100
        percentage_frequency[char] = round(percentage, 1)

    sorted_percentage_frequency = sorted(percentage_frequency.items())
    return sorted_percentage_frequency 
