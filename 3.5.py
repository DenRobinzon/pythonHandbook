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

# F.
# G.
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