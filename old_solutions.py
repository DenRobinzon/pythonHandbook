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

# H.Кашееды — 4

faf = {}
while line := input():
    for word in line.split():
        faf[word] = faf.setdefault(word, 0) + 1
for a, b in faf.items():
    print(a, b)


