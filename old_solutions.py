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

# Q.
# R.
# S.
# T.





