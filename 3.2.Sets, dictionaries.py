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



