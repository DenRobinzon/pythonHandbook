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

# H.
# I.
# J.
# K.
# L.
# M.
# N.
# O.
# P.
# Q.
# R.
# S.
# T.