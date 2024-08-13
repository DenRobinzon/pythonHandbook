# A.Символическая выжимка

print(''.join(set(input())))

# B.Символическая разница

print(''.join(set(input()).intersection(set(input()))))

# C.Зайка — 8

objects = set()
for _ in range(int(input())):
    objects = objects.union(set(input().split()))

print('\n'.join(objects))

# D.Кашееды

semolina_lovers = set()
oatmeal_lovers = set()

number_sl, number_ol = int(input()), int(input())

for _ in range(number_sl):
    semolina_lovers.add(input())

for _ in range(number_ol):
    oatmeal_lovers.add(input())

both_lovers = semolina_lovers & oatmeal_lovers

if both_lovers:
    print(len(both_lovers))
else:
    print('Таких нет')

# E.Кашееды — 2

number_of_children = int(input()) + int(input())
one_lovers = set()

for _ in range(number_of_children):
    name = input()
    if name in one_lovers:
        one_lovers.remove(name)
    else:
        one_lovers.add(name)

if one_lovers:
    print(len(one_lovers))
else:
    print('Таких нет')

# E.Кашееды — 2 - математическое решение

n, m = int(input()), int(input())
names = set()
for _ in range(n + m):
    names.add(input())

k = len(names)

res = 2 * k - n - m

print(res if res else 'Таких нет')

# F.Кашееды — 3

num_semolina_lovers = int(input())
num_oatmeal_lovers = int(input())
one_lovers = set()

for _ in range(num_oatmeal_lovers + num_semolina_lovers):
    name = input()
    if name in one_lovers:
        one_lovers.remove(name)
    else:
        one_lovers.add(name)

if one_lovers:
    for name in sorted(one_lovers):
        print(name)
else:
    print('Таких нет')

# G.Азбука Морзе

ABC_morze = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
}

text = input()

for char in text.upper():
    if char == ' ':
        print()
    else:
        print(ABC_morze[char], end=' ')

# H.Кашееды — 4

children_and_cereals = {}

for i in range(int(input())):
    input_data = input().split()
    children_and_cereals[input_data[0]] = input_data[1:]

cereal_required = input()

children_recuired = set()
for child, cereals in children_and_cereals.items():
    if cereal_required in cereals:
        children_recuired.add(child)

print(*sorted(children_recuired) if children_recuired else ('Таких нет', ), sep='\n')

#  I.Зайка — 9
frequency = {}
while (things := input().split()):
    for thing in things:
        frequency[thing] = frequency.get(0) + 1

for thing, number in frequency.items():
    print(thing, number)

# J.Транслитерация

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

input_text = input()
output_text = ''
for ch in input_text:
    if ch.upper() in TRANS_DICT:
        if ch.isupper():
            output_text += TRANS_DICT[ch.upper()].capitalize()
        else:
            output_text += TRANS_DICT[ch.upper()].lower()
    else:
        output_text += ch
print(output_text)

# K.Однофамильцы

names = {}
number_of_namesakes = 0

for _ in range(int(input())):
    name = input()
    names[name] = names.get(name, 0) + 1

for count in names.values():
    if count > 1:
        number_of_namesakes += count

print(number_of_namesakes)

# L.Однофамильцы — 2

names = {}
number_of_samenames = 0

for _ in range(int(input())):
    name = input()
    names[name] = names.get(name, 0) + 1

for name in sorted(names):
    if names[name] > 1:
        print(f'{name} - {names[name]}')
        number_of_samenames += 1

if not number_of_samenames:
    print('Однофамильцев нет')

# M.Дайте чего-нибудь новенького!

dishes = set()

for _ in range(int(input())):
    dishes.add(input())

for _ in range(int(input())):
    for _ in range(int(input())):
        dishes.discard(input())

if dishes:
    print(*sorted(dishes), sep='\n')
else:
    print('Готовить нечего')

# N.Это будет шедевр!

ingridients = set()
recipes = {}

for _ in range(int(input())):
    ingridients.add(input())

for _ in range(int(input())):
    dish = input()
    recipes[dish] = set()
    for _ in range(int(input())):
        recipes[dish].add(input())
    if not ingridients >= recipes[dish]:
        del recipes[dish]

if recipes:
    print(*sorted(recipes), sep='\n')
else:
    print('Готовить нечего')

# O.Двоичная статистика!

numbers = input().split()
stat = []

for number in numbers:
    number = str(bin(int(number)))[2:]
    stat.append({"digits": len(number), "units": number.count('1'),
                 "zeros": number.count('0')})

print(stat)

# P.Зайка — 10

bunny_neighbours = set()

while units := input().split():
    for _ in range(units.count('зайка')):
        bunny_index = units.index('зайка')
        if bunny_index > 0:
            bunny_neighbours.add(units[bunny_index - 1])
        if bunny_index < len(units) - 1:
            bunny_neighbours.add(units[bunny_index + 1])
        del units[bunny_index]
print(*bunny_neighbours, sep="\n")

# Q.Друзья друзей

friends_1 = {}

while names := input().split():
    name1, name2 = names
    friends_1.setdefault(name1, set()).add(name2)
    friends_1.setdefault(name2, set()).add(name1)

friends_2 = {}

for friend_1 in friends_1:
    friends_2[friend_1] = set()
    for friend_2 in friends_1[friend_1]:
        friends_2[friend_1].update(friends_1[friend_2] - {friend_1} - friends_1[friend_1])


for name in sorted(friends_2):
    print(f'{name}: {', '.join(sorted(friends_2[name]))}')

# R.Карта сокровищ

points = {}
for i in range(int(input())):
    x, y = input().split()
    key = (x[:-1], y[:-1])
    points[key] = points.get(key, 0) + 1

print(max(points.values()))

# S.Частная собственность

toys = {}

for _ in range(int(input())):
    input_string = input()
    new_toys = set(input_string[input_string.index(':') + 2:].split(', '))
    for toy in new_toys:
        toys[toy] = toys.get(toy, 0) + 1

for toy in sorted(toys):
    if toys[toy] == 1:
        print(toy)

# T.Простая задача 4.0

mutually_prime_numbers = {}
numbers_n_dividers = {}
numbers = []
numbers_str = input().split('; ')

for number in numbers_str:
    numbers.append(int(number))
numbers.sort()

for number in numbers:
    numbers_n_dividers[number] = []
    for div in range(1, number + 1):
        if number % div == 0:
            numbers_n_dividers[number].append(div)

for number1 in numbers:
    mutually_prime_numbers[number1] = set()
    for number2 in numbers:
        if len(set(numbers_n_dividers[number1]) & set(numbers_n_dividers[number2])) == 1:
            mutually_prime_numbers[number1].add(number2)

for number in mutually_prime_numbers:
    if mutually_prime_numbers[number]:
        print(number, ' - ', sep='', end='')
        print(*sorted(mutually_prime_numbers[number]), sep=', ')




