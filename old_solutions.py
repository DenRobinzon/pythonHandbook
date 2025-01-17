# 2.2. Условный оператор

# A.Просто здравствуй, просто как дела

name = input('Как Вас зовут?\n')
print(f'Здравствуйте, {name}!')
mood = input('Как дела?\n')
match mood:
    case 'хорошо':
        print('Я за вас рада!')
    case 'плохо':
        print('Всё наладится!')

# B.Кто быстрее?

sp, sv = int(input()), int(input())
if sp > sv:
    print('Петя')
else:
    print('Вася')

# C.Кто быстрее на этот раз?

sp, sv, st = int(input()), int(input()), int(input())
ms = max(sp, sv, st)

if ms == sp:
    print('Петя')
elif ms == sv:
    print('Вася')
elif ms == st:
    print('Толя')
else:
    print('Непонятно')

# D.Список победителей

sp, sv, st = int(input()), int(input()), int(input())
w = max(sp, sv, st)
ls = min(sp, sv, st)
if sp == w:
    print('1. Петя')
    if st == ls:
        print('2. Вася')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Вася')
elif sv == w:
    print('1. Вася')
    if st == ls:
        print('2. Петя')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Петя')
else:
    print('1. Толя')
    if sp == ls:
        print('2. Вася')
        print('3. Петя')
    else:
        print('2. Петя')
        print('3. Вася')

# E.Яблоки

n, m = int(input()), int(input())
if n > 6 + m:
    print('Петя')
else:
    print('Вася')

# F.Сила прокрастинации

year = int(input())
if year % 100 == 0:
    if year % 400 == 0:
        print('YES')
    else:
        print('NO')
else:
    if year % 4 == 0:
        print('YES')
    else:
        print('NO')

# G.А роза упала на лапу Азора

num = int(input())
a = num // 1000
b = num % 1000 // 100
c = num % 100 // 10
d = num % 10
if a == d and b == c:
    print('YES')
else:
    print('NO')

# H.Зайка — 1

phrase = input()
if 'зайка' in phrase:
    print('YES')
else:
    print('NO')

# I.Первому игроку приготовиться

a, b, c = input(), input(), input()
print(min(a, b, c))

# J.Лучшая защита — шифрование

num = input()
a = int(num[0]) + int(num[1])
b = int(num[1]) + int(num[2])
if a > b:
    print(str(a) + str(b))
else:
    print(str(b) + str(a))

# K.Красота спасёт мир

num = input()
a = int(num[0])
b = int(num[1])
c = int(num[2])
mx = max(a, b, c)
mn = min(a, b, c)
md = a + b + c - mn - mx

if mn + mx == md * 2:
    print('YES')
else:
    print('NO')

# L.Музыкальный инструмент

a, b, c = int(input()), int(input()), int(input())
mx = max(a, b, c)
mn = min(a, b, c)
md = a + b + c - mn - mx

if mx < md + mn:
    print('YES')
else:
    print('NO')

# M.Властелин Чисел: Братство общей цифры

a, b, c = input(), input(), input()
if a[0] in b and a[0] in c:
    print(a[0])
else:
    print(a[1])

# N.Властелин Чисел: Две Башни

num = input()
a = int(num[0])
b = int(num[1])
c = int(num[2])
mx = max(a, b, c)
mn = min(a, b, c)
md = a + b + c - mn - mx

if mn == 0 and md == 0:
    print(str(mx) + str(mn), str(mx) + str(md))
elif mn == 0:
    print(str(md) + str(mn), str(mx) + str(md))
else:
    print(str(mn) + str(md), str(mx) + str(md))

# O.Властелин Чисел: Возвращение Цезаря

a, b = input()
c, d = input()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
mx = max(a, b, c, d)
mn = min(a, b, c, d)
print(str(mx) + str((a + b + c + d - mx - mn) % 10) + str(mn))

# P.Легенды велогонок возвращаются: кто быстрее?

sp, sv, st = int(input()), int(input()), int(input())
if sp > sv and sp > st:
    wn = 'Петя'
    if sv > st:
        md, ls = 'Вася', 'Толя'
    else:
        md, ls = 'Толя', 'Вася'
elif sv > st and sv > sp:
    wn = 'Вася'
    if sp > st:
        md, ls = 'Петя', 'Толя'
    else:
        md, ls = 'Толя', 'Петя'
else:
    wn = 'Толя'
    if sp > sv:
        md, ls = 'Петя', 'Вася'
    else:
        md, ls = 'Вася', 'Петя'
print(f'{wn:^24}')
print(f'{md:^8}')
print(' ' * 16 + f'{ls:^8}')
print('II'.center(8) + 'I'.center(8) + 'III'.center(8))

# Q.Корень зла

a, b, c = float(input()), float(input()), float(input())
if a == 0:
    if b == 0:
        if c == 0:
            print('Infinite solutions')
        else:
            print('No solution')
    else:
        x = -c / b
        print(round(x, 2))
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('No solution')
    elif d == 0:
        x = -b / (2 * a)
        print(round(x, 2))
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(*sorted((round(x1, 2), round(x2, 2))))

# 2.3.Циклы

# C.Считалочка

for i in range(int(input()), int(input()) + 1):
    print(i, end=' ')

# D.Считалочка 2.0

a, b = int(input()), int(input())

if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
elif a > b:
    for i in range(a, b - 1, -1):
        print(i, end=' ')
else:
    print(a)

# E.Внимание! Акция!

sum = 0

while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
    sum += price
print(sum)

# F.НОД

a, b = int(input()), int(input())
mx = max(a, b)
mn = min(a, b)
while mx % mn != 0:
    ost = mx % mn
    mx, mn = mn, ost
print(mn)

# G.НОК

a, b = int(input()), int(input())
mx = max(a, b)
mn = min(a, b)
while mx % mn != 0:
    ost = mx % mn
    mx, mn = mn, ost
print(int(a * b / mn))

# H.Излишняя автоматизация 2.0

inf, n = input(), int(input())
for i in range(n):
    print(inf)

# I.Факториал

num = int(input())
fac = 1
for i in range(1, num + 1):
    fac *= i
print(fac)

# J.Маршрут построен

x, y = 0, 0
while (dr := input()) != 'СТОП':
    if dr == 'СЕВЕР':
        y += int(input())
    elif dr == 'ЮГ':
        y -= int(input())
    elif dr == 'ВОСТОК':
        x += int(input())
    else:
        x -= int(input())
print(y, x, sep='\n')

# K.Цифровая сумма

num = input()
sm = 0
for n in num:
    sm += int(n)
print(sm)

# L.Сильная цифра

num = input()
mx = int(num[0])
for n in num[1:]:
    if int(n) > mx:
        mx = int(n)
print(mx)

# M.Первому игроку приготовиться 2.0

n, mnname = int(input()), input()
for i in range(n - 1):
    if (name := input()) < mnname:
        mnname = name
print(mnname)


# N.Простая задача
n = int(input())
f = 0
if n == 1:
    f = 1
else:
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            f = 1
            break
print('NO' if f else 'YES')

# O.Зайка-4

n, c = int(input()), 0
for _ in range(n):
    if 'зайка' in (phrase := input()):
        c += 1
print(c)

# P.А роза упала на лапу Азора 2.0

num = input()
f = 'YES'
for i in range(len(num) // 2):
    if num[i] != num[-i - 1]:
        f = 'NO'
print(f)

# Q.Четная чистота

num = input()
newnum = ''
for i in num:
    if int(i) % 2 != 0:
        newnum += i
print(newnum)

# 2.4.Вложенные циклы

# A.Таблица умножения

num = int(input())
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i * j, end=' ')
    print()

# B.Не таблица умножения
num = int(input())
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f'{j} * {i} = {i * j}')

# D.Суммарная сумма

n = int(input())
sum = 0
for i in range(n):
    num = input()
    for j in num:
        sum += int(j)
print(sum)

# E.Зайка-5

count = 0
for _ in range(int(input())):
    flag = False
    while True:
        word = input()
        if word == 'ВСЁ':
            break
        if word.lower() == 'зайка':
            flag = True
    count += flag
print(count)

# M.Числовой прямоугольник 2.0

num1, num2 = int(input()), int(input())
ln = len(str(num1 * num2))
for i in range(1, num1 + 1):
    for j in range(num2):
        n = i + num1 * j
        print(str(n).rjust(ln), end=' ')
    print()

# N.Числовая змейка

num1, num2 = int(input()), int(input())
width = len(str(num1 * num2))
n = 0
for i in range(num1):
    strt = ''
    if not i % 2:
        for _ in range(num2):
            n += 1
            strt += str(n).rjust(width) + ' '
    else:
        for _ in range(num2):
            n += 1
            strt = str(n).rjust(width) + ' ' + strt
    print(strt)

# N.Числовая змейка 2.0

n1, n2 = int(input()), int(input())
width = len(str(n1 * n2))
for i in range(1, n1 + 1):
    st = ''
    n = 0
    for j in range(n2):
        if j % 2:
            st += str(n1 + n1 * j - i + 1).rjust(width) + ' '
        else:
            st += str(i + n1 * j).rjust(width) + ' '
    print(st)

# 3.1. Строки, кортежи, списки

# A.Азбука

flag = True
for _ in range(int(input())):
    if input()[0].lower() not in 'абв':
        flag = False
print('YES' if flag else 'NO')

# B.Кручу-верчу

for ch in input():
    print(ch)

# C.Анонс новости

le = int(input())
for _ in range(int(input())):
    title = input()
    if len(title) > le:
        print(title[:le - 3] + '...')
    else:
        print(title)

# D.Очистка данных

while st := input():
    if st.endswith('@@@'):
        continue
    elif st.startswith('##'):
        print(st[2:])
    else:
        print(st)

# E.А роза упала на лапу Азора 4.0

st = input()
print("YES" if st == st[::-1] else 'NO')

# F.Зайка — 6

counter = 0
for _ in range(int(input())):
    counter += input().count('зайка')
print(counter)

# G.А и Б сидели на трубе

print(sum(int(i) for i in input().split()))

# H.Зайка — 7

for _ in range(int(input())):
    res = input().find('зайка')
    if res != -1:
        print(res + 1)
    else:
        print('Заек нет =(')

# I.Без комментариев

while st := input():
    if '#' in st:
        if st.startswith('#'):
            continue
        else:
            print(st[:st.find('#')])
    else:
        print(st)

# J.Частотный анализ на минималках

words = ''
letters = ''
winletter = 'а'
winscore = 0
while (word := input()) != 'ФИНИШ':
    words += word
words = words.lower().replace(' ', '')
for i in words:
    if i not in letters:
        letters += i
        score = words.count(i)
        if score > winscore or (score == winscore and ord(i) < ord(winletter)):
            winletter = i
            winscore = score

print(winletter)

# K.Найдется всё

s = []
for _ in range(int(input())):
    s.append(input())
q = input().lower()
for i in s:
    if q in i.lower():
        print(i)

# L.Меню питания

s = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
n = int(input())
for i in range(n):
    print(s[i % 5])

# M.Массовое возведение в степень

lst = []
for _ in range(int(input())):
    lst.append(int(input()))
d = int(input())
for i in lst:
    print(i ** d)

# N.Массовое возведение в степень 2.0

numbers = [int(i) for i in input().split()]
d = int(input())
for i in numbers:
    print(i ** d, end=' ')

# O.НОД 3.0 - не решена

# P.Анонс новости 2.0 - не решена

# P.Анонс новости 2.0
title = ''
length = int(input())
number_of_strings = int(input())

for i in range(number_of_strings):
    title += input() + '\n'

if len(title) - (new_line_ch := title.count('\n')) > length:
    print(title[:(length + new_line_ch - 3)] + '...')
else:
    print(title)

# Q.А роза упала на лапу Азора 5.0

string = input().replace(' ', '').lower()
print('YES' if string == string[::-1] else 'NO')

# R.RLE

lst = []
line = input()
ch = line[0]
for i in line[1:]:
    if i == ch[0]:
        ch += i
    else:
        print(ch[0], len(ch))
        ch = i
print(ch[0], len(ch))

# 3.2.Множества, словари

# A.Символическая выжимка

print(''.join(set(input())))

# B.Символическая разница

a = set(input())
b = set(input())
c = a & b
print(''.join(c))

# C.Зайка — 8

s = set()
for _ in range(int(input())):
    s.update(input().split())
print(*s, sep='\n')

# D.Кашееды

n, m = int(input()), int(input())
mnk, ovs = set(), set()
for _ in range(n):
    mnk.add(input())
for _ in range(m):
    ovs.add(input())
res = mnk & ovs
print(len(res) if res else 'Таких нет')

# E.Кашееды — 2

n, m = int(input()), int(input())
names = set()
for _ in range(n + m):
    names.add(input())

k = len(names)

res = 2 * k - n - m

print(res if res else 'Таких нет')

# F.Кашееды — 3

n, m = int(input()), int(input())
names = set()
for _ in range(n + m):
    name = input()
    if name in names:
        names.remove(name)
    else:
        names.add(name)
print(*sorted(names) if names else ('Таких нет', ), sep='\n')

# G.Азбука Морзе

# H.Кашееды — 4 интересное решение наоборот
kasha = {}
for _ in range(int(input())):
    name, *kashas = input().split()
    for k in kashas:
        kasha[k] = kasha.get(k, []) + [name]

res = kasha.get(input(), ('Таких нет',))
print(*sorted(res), sep='\n')


faf = {}
while line := input():
    for word in line.split():
        faf[word] = faf.setdefault(word, 0) + 1
for a, b in faf.items():
    print(a, b)


#  I.Зайка — 9

# J.Транслитерация

gost = {
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

line = input()
for ch in line:
    if ch.upper() in gost:
        if ch.upper() == ch:
            print(gost[ch.upper()].lower().capitalize(), end='')
        else:
            print(gost[ch.upper()].lower(), end='')
    else:
        print(ch, end='')

# K.Однофамильцы

sim_sur = {}
res = 0
for _ in range(int(input())):
    name = input()
    sim_sur[name] = sim_sur.setdefault(name, 0) + 1
for name in sim_sur:
    if sim_sur[name] > 1:
        res += sim_sur[name]
print(res)

# L.Однофамильцы — 2

sim_sur = {}
res = []
for _ in range(int(input())):
    name = input()
    sim_sur[name] = sim_sur.setdefault(name, 0) + 1
for name, n in sim_sur.items():
    if n > 1:
        res.append((name, n))
if res:
    for i in sorted(res):
        print(f'{i[0]} - {i[1]}')
else:
    print('Однофамильцев нет')


# M.Дайте чего-нибудь новенького!

dishes = set()
for _ in range(int(input())):
    dishes.add(input())
for _ in range(int(input())):
    for _ in range(int(input())):
        dishes.discard(input())
print(*sorted(dishes) if dishes else ('Готовить нечего',), sep='\n')

# N.Это будет шедевр!

prod = []
rec = {}
for _ in range(int(input())):
    prod.append(input())
for _ in range(int(input())):
    name = input()
    for _ in range(int(input())):
        rec[name] = rec.setdefault(name, []) + [input()]
    if not set(rec[name]) <= set(prod):
        del rec[name]
print(*sorted(rec) if rec else ('Готовить нечего',), sep='\n')

# O.Двоичная статистика!

nums = input().split()
res = []
for i in nums:
    ib = str(bin(int(i)))[2:]
    res.append({'digits': len(ib), 'units': ib.count('1'), 'zeros': ib.count('0')})
print(res)

# P.Зайка — 10

res = set()
while lines := input().lower().split():
    while 'зайка' in lines:
        i = lines.index('зайка')
        del lines[i]
        if i < 1:
            iq = 1
        else:
            iq = i
        res.update(lines[iq - 1:i + 1])

print(*res, sep='\n')

# Q.Друзья друзей

frnds = {}

while line := input().split():
    a, b = line
    frnds[a] = frnds.setdefault(a, set()) | {b}
    frnds[b] = frnds.setdefault(b, set()) | {a}
frnds2 = {}

for i in frnds:
    frnds[i].discard(i)
    for j in frnds[i]:
        frnds2[i] = frnds2.setdefault(i, set()) | frnds[j]
    frnds2[i] -= frnds[i] | {i}

for i in sorted(frnds2):
    print(f"{i}: {', '.join(sorted(frnds2[i]))}")

# R.Карта сокровищ

crd = {}
for _ in range(int(input())):
    x, y = (int(i) // 10 for i in input().split())
    crd[(x, y)] = crd.setdefault((x, y), 0) + 1
print(max(crd.values()))

# S.Частная собственность

d = {}
for _ in range(int(input())):
    name, toys = input().split(': ')
    toys_set = set(toys.split(', '))
    for t in toys_set:
        d[t] = d.setdefault(t, 0) + 1

print(*sorted(t for t in d if d[t] == 1), sep='\n')

# T.Простая задача 4.0

d = {}
nums = sorted({int(x) for x in input().split('; ')})
d2 = {}
for n in nums:
    if n == 0:
        d[n] == [0]
    elif n in (1, -1):
        d[n] = []
    else:
        for n1 in range(2, n + 1):
            if n % n1 == 0:
                d[n] = d.setdefault(n, []) + [n1]

for i in d:
    if i == 0:
        d2[i] = nums
    for j in d:
        if j == 0:
            d2[i] = [0]
        elif len(set(d[i]) & set(d[j])) == 0:
            d2[i] = d2.setdefault(i, []) + [j]
for i in d2:
    print(f"{i} - {', '.join(str(y) for y in d2[i])}")

# 3.3.Списочные выражения. Модель памяти для типов языка Python

# A.Список квадратов

[x ** 2 for x in range(a, b + 1)]

# B.Таблица умножения 2.0

[[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

# C.Длины всех слов

[len(word) for word in sentence.split()]

# D.Множество нечетных чисел
{x for x in numbers if x % 2 != 0}

# E.Множество всех полных квадратов
{x for x in numbers if not (a := (x ** 0.5)) - int(a)}

# F.Буквенная статистика
{letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()}

# G.Делители
{n: [i for i in range(1, n + 1) if n % i == 0] for n in numbers}

# H.Аббревиатура
''.join(word[0].upper() for word in string.split())

# I.Преобразование в строку
' - '.join([str(n) for n in sorted(set(numbers))])

# J.RLE наоборот
''.join(letter * n for letter, n in rle)

# 3.4. Встроенные возможности по работе с коллекциями

# A.Автоматизация списка
print(*[f'{n}. {item}' for n, item in enumerate(input().split(), 1)], sep='\n')


# B.Сборы на прогулку
print(*(f'{name_1} - {name_2}' for name_1, name_2 in zip(input().split(', '), input().split(', '))), sep='\n')

# C.Рациональная считалочка
from itertools import count

start, end, step = (float(x) for x in input().split())

for n in count(start, step):
    if n <= end:
        print(n)
    else:
        break
# D.Словарная ёлка

from itertools import accumulate

for line in accumulate((x + ' ' for x in input().split())):
    print(line)

# E.Список покупок

from itertools import chain

print(*(f'{index}. {product}' for index, product in enumerate(sorted(chain(input().split(', '),
                                                                           input().split(', '),
                                                                           input().split(', '))), 1)), sep='\n')
# F.Колода карт

from itertools import product

suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
print(*(f'{v} {s}' for v, s in list(product(values, suits))), sep='\n')


# G.Игровая сетка
from itertools import combinations

names = [input() for _ in range(int(input()))]

for name_1, name_2 in combinations(names, 2):
    print(f'{name_1} - {name_2}')


# H.Меню питания 2.0

from itertools import cycle

cerials = [input() for _ in range(int(input()))]
counter = 0
n = int(input())
for cerial in cycle(cerials):
    if counter < n:
        print(cerial)
        counter += 1
    else:
        break

# I.Таблица умножения 3.0
from itertools import product
n = int(input())
nums = (a * b for a, b in product(range(1, n + 1), range(1, n + 1)))
for i, num in enumerate(nums):
    if i % n == 0 and i != 0:
        print()
    print(num, end=' ')

# J.
# K.
# L.Список покупок 2.0
goods = []

for _ in range(int(input())):
    if (g := input().split(', ')) == 1:
        goods.append(g)
    else:
        goods.extend(g)
for i, g in enumerate(sorted(goods), 1):
    print(f'{i}. {g}')
# M.Расстановка спортсменов
from itertools import permutations

names = [input() for _ in range(int(input()))]
for i in sorted(permutations(names)):
    print(*i, sep=', ')

# N.Спортивные гадания
from itertools import permutations

names = [input() for _ in range(int(input()))]
for i in sorted(permutations(names, 3)):
    print(*i, sep=', ')

# O.Список покупок 3.0
from itertools import combinations, permutations

goods = set()
goods2 = set()
for _ in range(int(input())):
    goods.update(input().split(', '))
for i in combinations(goods, 3):
    for j in permutations(i):
        goods2.add(j)
for i in sorted(goods2):
    print(*i)

# P.Расклад таков...


# Q.А есть ещё варианты?
# R.Таблица истинности
from itertools import product

st = input()
print('a b c f')
for a, b, c in product((0, 1), (0, 1), (0, 1)):
    exec(f'f = {st}')
    print(f'{a} {b} {c} {int(f)}')

# S.Таблица истинности 2


# T.

# 3.5. Потоковый ввод/вывод. Работа с текстовыми файлами. JSON
# A.A+B+...

from sys import stdin

print(sum(int(i) for i in stdin.read().split()))

# B.Средний рост
from sys import stdin
n, d = 0, 0
for line in stdin:
    _, h, h1 = line.split()
    d += int(h1) - int(h)
    n += 1
print(round(d / n))

# C.Без комментариев 2.0
from sys import stdin

for line in stdin.readlines():
    if line.lstrip() and line.rstrip()[0] == '#':
        continue
    else:
        print(line.split('#')[0].rstrip())

# D.Найдётся всё 2.0
from sys import stdin

lines = [i.rstrip() for i in stdin.readlines()]
for line in lines[:-1]:
    if lines[-1].lower() in line.lower():
        print(line)

# E.А роза упала на лапу Азора 6.0
from sys import stdin

pal = {word for word in stdin.read().split() if word.lower() == word.lower()[::-1]}

print(*sorted(pal), sep='\n')
# F.Транслитерация 2.0
chars = {
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

with open('cyrillic.txt', encoding='UTF-8') as file_in:
    srstext = file_in.read()
    text = ''
    for ch in srstext:
        if ch.isalpha() and ch.upper() in chars:
            ch2 = chars[ch.upper()]
            if ch.isupper():
                text += ch2.lower().capitalize()
            else:
                text += ch2.lower()
        else:
            text += ch

with open('transliteration.txt', 'w', encoding='UTF-8') as file_out:
    file_out.write(text)


# G.Файловая статистика
with open(f'{input()}', encoding='UTF-8') as file_in:
    numbers = [int(i) for i in file_in.read().split()]

print(a := len(numbers))
print(len([n for n in numbers if n > 0]))
print(min(numbers))
print(max(numbers))
print(b := sum(numbers))
print(round(b / a, 2))
# H.Файловая разница
with open(f'{input()}', encoding='UTF-8') as file_in:
    first = set(file_in.read().split())

with open(f'{input()}', encoding='UTF-8') as file_in:
    second = set(file_in.read().split())

    third = first ^ second

with open(f'{input()}', 'w', encoding='UTF-8') as file_out:
    print(*sorted(third), sep='\n', file=file_out)


# I.Файловая чистка
with open(f'{input()}', encoding='UTF-8') as file_in, \
        open(f'{input()}', 'w', encoding='UTF-8') as file_out:
    for line in file_in.readlines():
        line = line.replace('\t', '')
        line = ' '.join(line.split())
        if line:
            print(line, file=file_out)

# J.Хвост
with open(f'{input()}', encoding='UTF-8') as some_file:
    print(*some_file.readlines()[-int(input()):], sep='')

# K.Файловая статистика 2.0
import json

with open(f'{input()}', 'r', encoding='UTF-8') as file_in:
    nums = [int(i) for i in file_in.read().split()]

with open(f'{input()}', 'w', encoding='UTF-8') as file_out:
    result = {
        'count': len(nums),
        'positive_count': len([i for i in nums if i > 0]),
        'min': min(nums),
        'max': max(nums),
        'sum': sum(nums),
        'average': round(sum(nums) / len(nums), 2),
    }

    json.dump(result, file_out, ensure_ascii=False, indent=4)
# L.Разделяй и властвуй
def more_even(num):
    ne, no = 0, 0
    for c in num.lstrip('-'):
        if int(c) % 2 == 0:
            ne += 1
        else:
            no += 1
    if ne > no:
        return 'e'
    elif no > ne:
        return 'o'
    else:
        return 'eq'


with open(f'{input()}', encoding='UTF-8') as file_in, \
        open(f'{input()}', 'w', encoding='UTF-8') as file_e, \
        open(f'{input()}', 'w', encoding='UTF-8') as file_o, \
        open(f'{input()}', 'w', encoding='UTF-8') as file_eq:
    for line in file_in:
        e, o, eq = '', '', ''
        nums = line.split()
        for n in nums:
            if more_even(n) == 'e':
                print(n, file=file_e, end=' ')
            elif more_even(n) == 'o':
                print(n, file=file_o, end=' ')
            else:
                print(n, file=file_eq, end=' ')
        file_e.write('\n')
        file_o.write('\n')
        file_eq.write('\n')

# M.Обновление данных
import json
from sys import stdin

filename = input()
with open(filename, encoding='UTF-8') as file_in:
    res = json.load(file_in)

for line in stdin:
    k, v = line.rstrip().split(' == ')
    res[k] = v

with open(filename, 'w', encoding='UTF-8') as file_json:
    json.dump(res, file_json, ensure_ascii=False, indent=2, sort_keys=True)

# N.

# O.
# P.Найдётся всё 3.0
from sys import stdin
res = []

query = input().lower()
files = stdin.read().split()
for f in files:
    with open(f, encoding='UTF-8') as file_in:
        text = ' '.join(file_in.read().replace('&nbsp;', ' ').split()).lower()
        if query in text:
            res.append(f)
if res:
    print(*res, sep='\n')
else:
    print('404. Not Found')

# Q.Прятки
# R.Сколько вешать в байтах?
import os.path
import math

size = os.path.getsize(input())
if size < 1024:
    print(f'{math.ceil(size)}Б')
elif size < 1024 ** 2:
    print(f'{math.ceil(size / 1024)}КБ')
elif size < 1024 ** 3:
    print(f'{math.ceil(size / 1024 ** 2)}МБ')
else:
    print(f'{math.ceil(size / 1024 ** 3)}ГБ')

# S.Это будет наш секрет
k = int(input())

with open('public.txt', encoding='UTF-8') as file_in:
    text = file_in.read()

text2 = ''

for ch in text:
    i = k % 26 + ord(ch)
    if 65 <= ord(ch) <= 90:
        if i < 65:
            ch2 = chr(i + 26)
        elif 65 <= i <= 90:
            ch2 = chr(i)
        else:
            ch2 = chr(i - 26)

    elif 97 <= ord(ch) <= 122:
        if i < 97:
            ch2 = chr(i + 26)
        elif 97 <= i <= 122:
            ch2 = chr(i)
        else:
            ch2 = chr(i - 26)
    else:
        ch2 = ch
    text2 += ch2

with open('private.txt', 'w', encoding='UTF-8') as file_out:
    file_out.write(text2)


# T. Не решена

4.1. Функции. Области видимости. Передача параметров в функции
# A.Функциональное приветствие
def print_hello(name):
    print(f'Hello, {name}!')

# B.Функциональный НОД
def gcd(n1, n2):
    mn = max(n1, n2)
    k = min(n1, n2)
    while k:
        mx, mn = mn, k
        k = mx % mn
    return mn


# C.Длина числа
def number_length(num):
    return len(str(num).lstrip('-'))

# D.Имя of the month
def month(num, lang):
    m = {'en': ['January', 'February', 'March',
                'April', 'May', 'June',
                'July', 'August', 'September',
                'October', 'November', 'December'],
         'ru': ['Январь', 'Февраль', 'Март',
                'Апрель', 'Май', 'Июнь',
                'Июль', 'Август', 'Сентябрь',
                'Октябрь', 'Ноябрь', 'Декабрь']}

    return m[lang][num - 1]

# E.Числовая строка
def split_numbers(nums):
    return tuple(int(i) for i in nums.split())

# F.Модернизация системы вывода
def modern_print(line, lines=set()):
    if line not in lines:
        print(line)
        lines.add(line)

# G.Шахматный «обед» не решена

# H.А роза упала на лапу Азора 7.0
def is_palindrome(smth):
    if isinstance(smth, int):
        smth = str(smth)
    if smth == smth[::-1]:
        return True
    else:
        return False

# 4.2. Позиционные и именованные аргументы. Функции высших порядков. Лямбда-функции
# A.Генератор списков
def make_list(length, value=0):
    return [value for i in range(length)]

# B.Генератор матриц
def make_matrix(size, value=0):
    if type(size) is int:
        return [[value for i in range(size)] for i in range(size)]
    else:
        return [[value for i in range(size[0])] for j in range(size[1])]
# C.Не решена
# D.Имя of the month 2.0
def month(n, lang='ru'):
    m = {'en': ['January', 'February', 'March',
                'April', 'May', 'June',
                'July', 'August', 'September',
                'October', 'November', 'December'],
         'ru': ['Январь', 'Февраль', 'Март',
                'Апрель', 'Май', 'Июнь',
                'Июль', 'Август', 'Сентябрь',
                'Октябрь', 'Ноябрь', 'Декабрь']}
    return m[lang][n - 1]

# E.Подготовка данных
def to_string(*args, sep=' ', end='\n'):
    return f'{sep}'.join(str(i) for i in args) + f'{end}'

# F.Кофейня
def order(*args):
    res = 0
    rec = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1,
                     "milk": 3},
        "Макиато": {"coffee": 2,
                    "milk": 1},
        "Кофе по-венски": {"coffee": 1,
                           "cream": 2},
        "Латте Макиато": {"coffee": 1,
                          "milk": 2,
                          "cream": 1},
        "Кон Панна": {"coffee": 1,
                      "cream": 1},
    }
    for arg in args:
        flag = True
        for ing in rec[arg]:
            if in_stock[ing] < rec[arg][ing]:
                flag = False
                break
        if flag:
            res = arg
            for ing in rec[arg]:
                in_stock[ing] -= rec[arg][ing]
            break
    if res:
        return res
    else:
        return 'К сожалению, не можем предложить Вам напиток'

# G.В эфире рубрика «Эксперименты»
results = []


def enter_results(*args):
    for i in range(0, len(args), 2):
        results.append((args[i], args[i + 1]))


def get_sum():
    s1, s2 = 0, 0
    for x, y in results:
        s1 += x
        s2 += y
    return round(s1, 2), round(s2, 2)


def get_average():
    s1, s2 = 0, 0
    for x, y in results:
        s1 += x
        s2 += y
    return round(s1 / len(results), 2), round(s2 / len(results), 2)

# H.
lambda x: (len(x), x.lower())
# I.
lambda num: not sum(int(digit) for digit in str(num)) % 2


# 4.3. Рекурсия. Декораторы. Генераторы
# A.Рекурсивный сумматор
def recursive_sum(*args):
    if len(args) == 1:
        return args[0]
    return args[-1] + recursive_sum(*args[:-1])

# B.Рекурсивный сумматор цифр
def recursive_digit_sum(num):
    if num // 10 == 0:
        return int(num)
    return recursive_digit_sum(num // 10) + num % 10
# C.Многочлен N-ой степени
def make_equation(*args):
    if len(args) == 1:
        return f'{args[0]}'
    return f'({make_equation(*args[:-1])}) * x + {args[-1]}'
# D.Декор результата

def answer(f):

    def decorated(*args, **kwargs):
        return f'Результат функции: {f(*args, **kwargs)}'

    return decorated
# E.Накопление результата
# F.Сортировка слиянием
# G.Однотипность не порок

def same_type(func):
    def decorated(*args, **kwargs):
        t = type(args[0])
        for i in args[1:]:
            if t != type(i):
                print("Обнаружены различные типы данных")
                return
        return func(*args, **kwargs)
    return decorated
# H.Генератор Фибоначчи
def fibonacci(n):
    f, f1 = 0, 1
    for i in range(n):
        if i == 0:
            yield f
        elif i == 1:
            yield f1
        else:
            f, f1 = f1, f1 + f
            yield f1

# I.Циклический генератор
def cycle(lst):
    i = 0
    while True:
        yield lst[i]
        if i == len(lst) - 1:
            i = 0
        else:
            i += 1

# J."Выпрямление" списка
def make_linear(lst):
    lst2 = []
    for i in lst:
        if type(i) is list:
            lst2 += make_linear(i)
        else:
            lst2 += [i]
    return lst2
# 5.1. Объектная модель Python. Классы, поля и методы

# A.Классная точка

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# B.Классная точка 2.0

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        return round((((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5), 2)

# C.Не нажимай красную кнопку!

class RedButton:

    def __init__(self, n=0):
        self.n = n

    def click(self):
        print('Тревога!')
        self.n += 1

    def count(self):
        return self.n

# D.Работа не волк

class Programmer:
    salaries = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.salary = self.salaries[grade]
        self.money = 0
        self.exp = 0

    def work(self, time):
        self.exp += time
        self.money += time * self.salary

    def rise(self):
        if self.grade == 'Junior':
            self.grade = 'Middle'
            self.salary += 5
        elif self.grade == 'Middle':
            self.grade = 'Senior'
            self.salary += 5
        else:
            self.salary += 1

    def info(self):
        return f'{self.name} {self.exp}ч. {self.money}тгр.'
# E.Классный прямоугольник
class Rectangle:
    def __init__(self, a, c):
        self.a = a
        self.c = c

    def area(self):
        return round(abs((self.a[0] - self.c[0]) * (self.a[1] - self.c[1])), 2)

    def perimeter(self):
        return round(abs(self.a[0] - self.c[0]) * 2 + abs(self.a[1] - self.c[1]) * 2, 2)

# F.Классный прямоугольник 2.0
class Rectangle:

    def __init__(self, a, c):
        self.a = a
        self.c = c
        self.pos = min(self.a[0], self.c[0]), max(self.a[1], self.c[1])

    def area(self):
        return round(abs((self.a[0] - self.c[0]) * (self.a[1] - self.c[1])), 2)

    def perimeter(self):
        return round(abs(self.a[0] - self.c[0]) * 2 + abs(self.a[1] - self.c[1]) * 2, 2)

    def get_pos(self):
        return self.pos

    def get_size(self):
        return round(abs(self.a[0] - self.c[0]), 2), round(abs(self.a[1] - self.c[1]), 2)

    def move(self, dx, dy):
        self.a = (round(self.a[0] + dx, 2), round(self.a[1] + dy, 2))
        self.c = (round(self.c[0] + dx, 2), round(self.c[1] + dy, 2))
        self.pos = min(self.a[0], self.c[0]), max(self.a[1], self.c[1])

    def resize(self, width, height):
        self.a = self.pos
        self.c = self.pos[0] + width, self.pos[1] - height

# G.Классный прямоугольник 3.0 не решена была
# H.Шашки
class Cell:

    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


class Checkers:

    def __init__(self):
        self.desk = {
            'A': {
                '8': 'X',
                '7': 'B',
                '6': 'X',
                '5': 'X',
                '4': 'X',
                '3': 'W',
                '2': 'X',
                '1': 'W',
            },
            'B': {
                '8': 'B',
                '7': 'X',
                '6': 'B',
                '5': 'X',
                '4': 'X',
                '3': 'X',
                '2': 'W',
                '1': 'X',
            },
            'C': {
                '8': 'X',
                '7': 'B',
                '6': 'X',
                '5': 'X',
                '4': 'X',
                '3': 'W',
                '2': 'X',
                '1': 'W',
            },
            'D': {
                '8': 'B',
                '7': 'X',
                '6': 'B',
                '5': 'X',
                '4': 'X',
                '3': 'X',
                '2': 'W',
                '1': 'X',
            },
            'E': {
                '8': 'X',
                '7': 'B',
                '6': 'X',
                '5': 'X',
                '4': 'X',
                '3': 'W',
                '2': 'X',
                '1': 'W',
            },
            'F': {
                '8': 'B',
                '7': 'X',
                '6': 'B',
                '5': 'X',
                '4': 'X',
                '3': 'X',
                '2': 'W',
                '1': 'X',
            },
            'G': {
                '8': 'X',
                '7': 'B',
                '6': 'X',
                '5': 'X',
                '4': 'X',
                '3': 'W',
                '2': 'X',
                '1': 'W',
            },
            'H': {
                '8': 'B',
                '7': 'X',
                '6': 'B',
                '5': 'X',
                '4': 'X',
                '3': 'X',
                '2': 'W',
                '1': 'X',
            },
        }

    def move(self, f, t):
        self.desk[t[0]][t[1]] = self.desk[f[0]][f[1]]
        self.desk[f[0]][f[1]] = 'X'

    def get_cell(self, p):
        return Cell(self.desk[p[0]][p[1]])

# I.Очередь

class Queue:

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return not bool(self.queue)
# J.Стек
class Stack:

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(-1)

    def is_empty(self):
        return not bool(self.queue)

# 5.2. Волшебные методы, переопределение методов. Наследование

# A.Классная точка 3.0
class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        return round((((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5), 2)


class PatchedPoint(Point):

    def __init__(self, x='n', y='n'):
        super().__init__(x, y)
        if x == 'n' and y == 'n':
            self.x = 0
            self.y = 0
        elif x != 'n' and y == 'n':
            self.x, self.y = self.x[0], self.x[1]

# B.Классная точка 4.0
class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        return round((((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5), 2)


class PatchedPoint(Point):

    def __init__(self, x='n', y='n'):
        super().__init__(x, y)
        if x == 'n' and y == 'n':
            self.x = 0
            self.y = 0
        elif x != 'n' and y == 'n':
            self.x, self.y = self.x[0], self.x[1]

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self):
        return f'PatchedPoint{self.x, self.y}'

# C.Классная точка 5.0
class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        return round((((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5), 2)


class PatchedPoint(Point):

    def __init__(self, x='n', y='n'):
        super().__init__(x, y)
        if x == 'n' and y == 'n':
            self.x = 0
            self.y = 0
        elif x != 'n' and y == 'n':
            self.x, self.y = self.x[0], self.x[1]

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self):
        return f'PatchedPoint{self.x, self.y}'

    def __add__(self, xy):
        return PatchedPoint(self.x + xy[0], self.y + xy[1])

    def __iadd__(self, xy):
        self.x += xy[0]
        self.y += xy[1]
        return self

# D.Дроби v0.1
class Fraction:

    def __init__(self, a, b='n'):
        if b == 'n':
            a, b = (int(i) for i in a.split('/'))
        x, y = a, b
        while y:
            x, y = y, x % y
        self._a = int(a / x)
        self._b = int(b / x)

    def numerator(self, num='n'):
        if num == 'n':
            return self._a
        else:
            a = num
            b = self._b

            x, y = a, b
            while y:
                x, y = y, x % y
            self._a = int(a / x)
            self._b = int(b / x)

    def denominator(self, num='n'):
        if num == 'n':
            return self._b
        else:
            a = self._a
            b = num
            x, y = a, b
            while y:
                x, y = y, x % y
            self._a = int(a / x)
            self._b = int(b / x)

    def __str__(self):
        return f'{self._a}/{self._b}'

    def __repr__(self):
        return f'Fraction({self._a}, {self._b})'

# E.Дроби v0.2

# 5.3. Модель исключений Python. Try, except, else, finally. Модули
# A.Обработка ошибок
try:
    func()
except ValueError as e:
    print('ValueError')
except TypeError as e:
    print('TypeError')
except SystemError as e:
    print('SystemError')
else:
    print('No Exceptions')

# B.Ломать — не строить
func('q', {1})

# C.Ломать — не строить 2
class Bad:
    def __init__(self):
        pass

    def __str__(self):
        raise Exception

    def __repr__(self):
        raise Exception


func(Bad())

# D.Контроль параметров
def only_int(*args):
    if not all(isinstance(i, int) for i in args):
        raise TypeError


def only_pos_ev(*args):
    if any(i % 2 != 0 for i in args) or any(i <= 0 for i in args):
        raise ValueError


def only_positive_even_sum(*args):
    only_int(*args)
    only_pos_ev(*args)
    return sum(args)

# E.Слияние с проверкой

def merge(a, b):
    if not all(hasattr(i, '__iter__') for i in (a, b)):
        raise StopIteration()

    if not (all(isinstance(i, type(a[0])) for i in a) and
            all(isinstance(i, type(a[0])) for i in b)):
        raise TypeError()

    if not all(list(i) == sorted(i) for i in (a, b)):
        raise ValueError()

    return (sorted(list(a) + list(b)))

# F.Корень зла 2 не решена

# G.Валидация имени
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    for i in name:
        if i.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            raise CyrillicError

    if name != name.capitalize():
        raise CapitalError

    return name

# H.Валидация имени пользователя
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError

    for i in name:
        if i.lower() not in 'abcdefghijklmnopqrstuvwqxyz1234567890_':
            raise BadCharacterError

    if name[0] in '1234567890':
        raise StartsWithDigitError

    return name

# I.Валидация пользователя
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    for i in name:
        if i.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            raise CyrillicError

    if name != name.capitalize():
        raise CapitalError

    return name


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError

    for i in name:
        if i.lower() not in 'abcdefghijklmnopqrstuvwqxyz1234567890_':
            raise BadCharacterError

    if name[0] in '1234567890':
        raise StartsWithDigitError

    return name


def user_validation(*args, **kwargs):
    if args or list(kwargs.keys()) != ['last_name', 'first_name', 'username']:
        raise KeyError

    name_validation(kwargs['last_name'])
    name_validation(kwargs['first_name'])
    username_validation(kwargs['username'])

    return kwargs

# J.Валидация пароля
from hashlib import sha256 as sha


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8,
                        possible_chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_',
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    for i in password:
        if i not in possible_chars:
            raise PossibleCharError

    if not any(at_least_one(i) for i in password):
        raise NeedCharError

    return sha(password.encode('utf-8')).hexdigest()

# 6.1. Модули math и numpy
# A.Математика — круто, но это не точно
import math


x = float(input())

res = (math.log(math.pow(x, 3 / 16), 32) +
       math.pow(x, math.cos(x * math.pi / (2 * math.e))) -
       math.pow(math.sin(x / math.pi), 2))


print(res)

# B.Потоковый НОД
from sys import stdin
import math


for line in stdin:
    print(math.gcd(*(int(i) for i in line.split())))

# C.Есть варианты? Не решена
# D.Среднее не арифметическое
import math


nums = [float(i) for i in input().split()]

print(math.pow(math.prod(nums), 1 / len(nums)))

# E.Шаг навстречу
import math


d = [float(i) for i in input().split()]
p = [float(i) for i in input().split()]

p2 = math.cos(p[1]) * p[0], math.sin(p[1]) * p[0]

print(math.pow((d[0] - p2[0]) ** 2 + (d[1] - p2[1]) ** 2, 0.5))

# F.Матрица умножения
import numpy as np


def multiplication_matrix(n):
    a1 = np.array([list(range(1, n + 1))] * n)
    a2 = np.rot90(a1, -1)
    return (a1 * a2)

# G.Шахматная подготовка
import numpy as np


def make_board(n):
    return np.array([[1, 0] * int(n / 2), [0, 1] * int(n / 2)] * int(n / 2), dtype='int8')

# H.Числовая змейка 3.0 не решена
# I.Вращение
import numpy as np


def rotate(mtrx, ang):
    for i in range(int(ang / 90)):
        mtrx = np.rot90(mtrx, -1)
    return mtrx

# J.Лесенка не решена
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