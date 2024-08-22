# 3.5. Потоковый ввод/вывод. Работа с текстовыми файлами. JSON
# A.A+B+...

from sys import stdin

print(sum(int(number) for number in stdin.read().split()))

# B.Средний рост
from sys import stdin

children = 0
total_growth = 0

for line in stdin:
    _, height_1, height_2 = line.split()
    total_growth += int(height_2) - int(height_1)
    children += 1

print(round(total_growth / children))

# C.Без комментариев 2.0
from sys import stdin

for line in stdin.readlines():
    if not line.startswith('#'):
        print(line.split('#')[0].rstrip('\n'))

# D.Найдётся всё 2.0
from sys import stdin

*lines, querry = stdin.readlines()

for line in lines:
    if querry.rstrip().lower() in line.lower():
        print(line, end='')

# E.А роза упала на лапу Азора 6.0
from sys import stdin

words = stdin.read().split()
palindromes = set(word for word in words if word.lower() == word.lower()[::-1])
print(*sorted(palindromes), sep='\n')

# F.Транслитерация 2.0
TRANS_DICT = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}

with open('cyrillic.txt', 'r', encoding='UTF-8') as file_in:
    text = file_in.read()

text_trans = ''

for char in text:
    if char.upper() in TRANS_DICT:
        if char.isupper():
            char = TRANS_DICT[char].capitalize()
        else:
            char = TRANS_DICT[char.upper()].lower()
    text_trans += char


with open('transliteration.txt', 'w', encoding='UTF-8') as file_out:
    print(text_trans, file=file_out)

# G.Файловая статистика
with open(input(), 'r', encoding='UTF-8') as file_in:
    numbers = [int(num) for num in file_in.read().split()]

count = len(numbers)
positive = len([num for num in numbers if num > 0])
min_number = min(numbers)
max_number = max(numbers)
total_sum = sum(numbers)
average = round(total_sum / count, 2)

print(count, positive, min_number, max_number, total_sum, average, sep='\n')

# H.Файловая разница
with open(input(), 'r', encoding='UTF-8') as file_in:
    words_1 = set(file_in.read().split())

with open(input(), 'r', encoding='UTF-8') as file_in:
    words_2 = set(file_in.read().split())

words_3 = sorted(words_1.symmetric_difference(words_2))

with open(input(), 'w', encoding='UTF-8') as file_out:
    print(*words_3, sep='\n', file=file_out)

# I.Файловая чистка
with open(input(), 'r', encoding='UTF-8') as file_in:
    lines = file_in.readlines()

new_lines = []

for line in lines:
    new_line = line.replace('\t', '')
    new_line = ' '.join(new_line.split())
    if new_line:
        new_lines.append(new_line)

with open(input(), 'w', encoding='UTF-8') as file_out:
    print(*new_lines, sep='\n', file=file_out)

# J.Хвост
with open(input(), 'r', encoding='UTF-8') as file_in:
    print(*file_in.readlines()[-int(input()):], sep='')

# K.Файловая статистика 2.0
import json

with open(input(), 'r', encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split()]

stats = {
    'count': len(numbers),
    'positive_count': len([number for number in numbers if number > 0]),
    'min': min(numbers),
    'max': max(numbers),
    'sum': sum(numbers),
    'average': round(sum(numbers) / len(numbers), 2)
}

with open(input(), 'w', encoding='UTF-8') as file_out:
    json.dump(stats, file_out, ensure_ascii=False, indent=2)

# L.Разделяй и властвуй
even_numbers = []
odd_numbers = []
eq_numbers = []

with open(input(), 'r', encoding='UTF-8') as file_in:
    for line in file_in:
        even_line = []
        odd_line = []
        eq_line = []
        for number in line.split():
            even_digits, odd_digits = 0, 0
            for digit in number:
                if int(digit) % 2:
                    odd_digits += 1
                else:
                    even_digits += 1
            if even_digits > odd_digits:
                even_line.append(number)
            elif even_digits < odd_digits:
                odd_line.append(number)
            else:
                eq_line.append(number)
        even_numbers.append(even_line)
        odd_numbers.append(odd_line)
        eq_numbers.append(eq_line)

with open(input(), 'w', encoding='UTF-8') as file_out:
    print('\n'.join((' '.join(numbers) for numbers in even_numbers)), file=file_out)

with open(input(), 'w', encoding='UTF-8') as file_out:
    print('\n'.join((' '.join(numbers) for numbers in odd_numbers)), file=file_out)

with open(input(), 'w', encoding='UTF-8') as file_out:
    print('\n'.join((' '.join(numbers) for numbers in eq_numbers)), file=file_out)

# только на строках

even_numbers = ''
odd_numbers = ''
eq_numbers = ''
evens = '08642'
with open(input(), 'r', encoding='UTF-8') as file_in:
    for line in file_in:
        even_line = ''
        odd_line = ''
        eq_line = ''
        for number in line.split():
            even_digits, odd_digits = 0, 0
            for digit in number:
                if digit in evens:
                    even_digits += 1
                else:
                    odd_digits += 1
            if even_digits > odd_digits:
                even_line += number + ' '
            elif even_digits < odd_digits:
                odd_line += number + ' '
            else:
                eq_line += number + ' '
        even_numbers += even_line + '\n'
        odd_numbers += odd_line + '\n'
        eq_numbers += eq_line + '\n'

with open(input(), 'w', encoding='UTF-8') as file_out:
    file_out.write(even_numbers)

with open(input(), 'w', encoding='UTF-8') as file_out:
    file_out.write(odd_numbers)

with open(input(), 'w', encoding='UTF-8') as file_out:
    file_out.write(eq_numbers)

# M.
# N.
# O.
# P.
# Q.
# R.
# S.
# T.