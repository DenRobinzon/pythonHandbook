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

# M.Обновление данных
import json
file_users, file_updates = input(), input()

with open(file_users, encoding='UTF-8') as file_in:
    users = json.load(file_in)

with open(file_updates, encoding='UTF-8') as file_in:
    updates = json.load(file_in)

users_new = {}

for user in users:
    for update in updates:
        if user["name"] == update["name"]:
            for k in update:
                if k not in user or update[k] > user[k]:
                    user[k] = update[k]
    users_new[user["name"]] = {k: v for k, v in user.items() if k != "name"}

with open(file_users, 'w', encoding='UTF-8') as file_out:
    json.dump(users_new, file_out, ensure_ascii=False, indent=4)

# N.Слияние данных
import json
file_users, file_updates = input(), input()

with open(file_users, encoding='UTF-8') as file_in:
    users = json.load(file_in)

with open(file_updates, encoding='UTF-8') as file_in:
    updates = json.load(file_in)

users_new = {}

for user in users:
    for update in updates:
        if user["name"] == update["name"]:
            for k in update:
                if k not in user or update[k] > user[k]:
                    user[k] = update[k]
    users_new[user["name"]] = {k: v for k, v in user.items() if k != "name"}

with open(file_users, 'w', encoding='UTF-8') as file_out:
    json.dump(users_new, file_out, ensure_ascii=False, indent=4)

# O.Поставь себя на моё место
import json
from sys import stdin

with open('scoring.json', encoding='UTF-8') as file_in:
    scoring = json.load(file_in)

answers = stdin.read().split()
score = 0

for group in scoring:
    points_for_test = group['points'] // len(group['tests'])
    for test in group['tests']:
        if test['pattern'] == answers.pop(0):
            score += points_for_test

print(score)

# P.Найдётся всё 3.0
from sys import stdin

query = input()
files = stdin.read().split()

query_modified = ''.join(query.split()).lower()
files_with_query = []

for file in files:
    with open(file, encoding='UTF-8') as file_in:
        content = ''.join(file_in.read().split()).lower()
        if query_modified in content:
            files_with_query.append(file)

if files_with_query:
    print(*files_with_query, sep='\n')
else:
    print('404. Not Found')

# Q.Прятки
with open('secret.txt', encoding='UTF-8') as file_in:
    text = file_in.read()

text_decoded = ''

for ch in text:
    code = ord(ch)
    if code > 128:
        code %= 256
    text_decoded += chr(code)

print(text_decoded)

# R.Сколько вешать в байтах?
import os

size = os.path.getsize(input())

unit = 'Б'

if size >= 1024 ** 3:
    size /= 1024 ** 3
    unit = 'ГБ'
elif size >= 1024 ** 2:
    size /= 1024 ** 2
    unit = 'МБ'
elif size >= 1024:
    size /= 1024
    unit = 'КБ'

if size > int(size):
    size = int(size) + 1
else:
    size = int(size)

print(size, unit, sep='')

# S.Это будет наш секрет
shift = int(input())
text_encoded = ''

with open('public.txt') as file_in:
    text = file_in.read()

for ch in text:
    code = ord(ch)
    if code in range(65, 91):
        code = (code - 65 + shift) % 26 + 65

    elif code in range(97, 123):
        code = (code - 97 + shift) % 26 + 97

    text_encoded += chr(code)

with open('private.txt', 'w') as file_out:
    file_out.write(text_encoded)

# T.Файловая сумма
sum_result = 0

with open('numbers.num', 'rb') as file_in:
    while (number := int.from_bytes(file_in.read(2))):
        sum_result += number

print(sum_result % 65536)
