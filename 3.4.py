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

# подсмотренное решение, но очень не интуитивное

from itertools import combinations

count = int(input())
nums = range(1, count)
print('А Б В')
for i, j in list(combinations(nums, 2)):
    print(f'{i} {j - i} {count - j}')
    print(i, j)

# K.Числовой прямоугольник 3.0

import itertools

height = int(input())
width = int(input())
ln = len(str(height * width))

nums = itertools.count(1)

for i in range(height * width):
    num = next(nums)
    print(f'{num:>{ln}}', end=' ')
    if num % width == 0:
        print()

# L.Список покупок 2.0
goods = []

for _ in range(int(input())):
    goods.extend(input().split(', '))

for i, thing in enumerate(sorted(goods), 1):
    print(f'{i}. {thing}')

# M.Расстановка спортсменов
import itertools

sportsmen = sorted([input() for _ in range(int(input()))])

print(*[', '.join(names) for names in itertools.permutations(sportsmen)], sep='\n')

# N.Спортивные гадания
import itertools

sportsmen = sorted([input() for _ in range(int(input()))])

print(*[', '.join(names) for names in itertools.permutations(sportsmen, 3)], sep='\n')

# O.Список покупок 3.0
import itertools

things_to_buy = []

for _ in range(int(input())):
    things_to_buy.extend(input().split(', '))

print(*[' '.join(things) for things in itertools.permutations(sorted(things_to_buy), 3)], sep='\n')


# P.Расклад таков...

import itertools

suits = {'буби': 'бубен',
         'пики': 'пик',
         'трефы': 'треф',
         'черви': 'червей'}

faces = ['10', '2', '3', '4', '5', '6', '7', '8',
         '9', 'валет', 'дама', 'король', 'туз']

suit = input()
face = input()

faces.remove(face)

cards = (' '.join(card) for card in itertools.product(faces, suits.values()))
selected_cards = (', '.join(selection) for selection in itertools.combinations(cards, 3))

counter = 10
while counter:
    string_to_print = next(selected_cards)
    if suits[suit] in string_to_print:
        print(string_to_print)
        counter -= 1

# решение получше, кое-что подсмотрел
import itertools

suits = {'буби': 'бубен',
         'пики': 'пик',
         'трефы': 'треф',
         'черви': 'червей'}

faces = ['10', '2', '3', '4', '5', '6', '7', '8',
         '9', 'валет', 'дама', 'король', 'туз']

suit = input()
face = input()

faces.remove(face)

cards = itertools.product(faces, suits.values())
three_cards = (selection for selection in itertools.combinations(cards, 3)
               if suits[suit] in itertools.chain.from_iterable(selection))

for three in itertools.islice(three_cards, 10):
    print(', '.join((f'{f} {s}' for f, s in three)))

# Q.А есть ещё варианты?
import itertools

suits = {'буби': 'бубен',
         'пики': 'пик',
         'трефы': 'треф',
         'черви': 'червей'}

faces = ['10', '2', '3', '4', '5', '6', '7', '8',
         '9', 'валет', 'дама', 'король', 'туз']

suit = input()
face = input()
previous_option = input()

faces.remove(face)

cards = itertools.product(faces, suits.values())
three_cards = (selection for selection in itertools.combinations(cards, 3)
               if suits[suit] in itertools.chain.from_iterable(selection))

printed = False

while not printed:
    if (', '.join((f'{f} {s}' for f, s in next(three_cards)))) == previous_option:
        print(', '.join((f'{f} {s}' for f, s in next(three_cards))))
        printed = True

# R.
# S.
# T.