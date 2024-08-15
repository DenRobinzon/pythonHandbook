# A.Автоматизация списка
print(*[f'{num}. {product}'
      for num, product in list(enumerate(input().split(), 1))], sep='\n')

# B.Сборы на прогулку
line1 = input().split(', ')
line2 = input().split(', ')

for child1, child2 in zip(line1, line2):
    print(f'{child1} - {child2}')

# C.Рациональная считалочка
import itertools

start, end, step = (float(num) for num in input().split())

for num in itertools.count(start, step):
    if num <= end:
        print(f'{num:.2f}')
    else:
        break

# D.Словарная ёлка
import itertools

words = input().split()

for i in itertools.count(1):
    if i <= len(words):
        print(' '.join(words[:i]))
    else:
        break

# покороче

from itertools import accumulate

for line in accumulate((word + ' ' for word in input().split())):
    print(line)

# E.Список покупок
products = set()

for _ in range(3):
    products.update(input().split(', '))

for i, product in enumerate(sorted(products), 1):
    print(f'{i}. {product}')

# в одну строку)

print(*(f'{index}. {product}' for index, product in enumerate(sorted(chain(input().split(', '),
                                                                           input().split(', '),
                                                                           input().split(', '))), 1)), sep='\n')
# F.Колода карт
import itertools

suits = ['пик', 'треф', 'бубен', 'червей']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']

suits.remove(input())

for value, suit in itertools.product(values, suits):
    print(value, suit)

# G.Игровая сетка

import itertools

names = [input() for _ in range(int(input()))]

for name1, name2 in itertools.combinations(names, 2):
    print(f'{name1} - {name2}')

# H.Меню питания 2.0

import itertools

cereals = [input() for _ in range(int(input()))]

days = int(input())

print('\n'.join(itertools.islice(itertools.cycle(cereals), days)))

# I.Таблица умножения 3.0

import itertools
size = int(input())

numbers = (num1 * num2 for num1, num2 in itertools.product(range(1, size + 1), repeat=2))

for i in range(size):
    print(*itertools.islice(numbers, size))

# J.Мы делили апельсин 2.0

import itertools

slices = int(input())

options = itertools.combinations_with_replacement('АБВ', slices - 3)

print('А Б В')

for option in sorted(options, reverse=True):
    print(f'{option.count('А') + 1} {option.count('Б') + 1} {option.count('В') + 1}')

# K.Числовой прямоугольник 3.0


# L.
# M.
# N.
# O.
# P.
# Q.
# R.
# S.
# T.